# HR Policy RAG Assistant

A retrieval-augmented Q&A system over an HR policy document, built to extend the 
single-document Q&A prompt from Week 1 into a real RAG pipeline — handling documents 
too large to paste into a single prompt, using retrieval to find relevant sections first.

## Stack (all free/local)
- **Chunking:** LangChain `RecursiveCharacterTextSplitter`
- **Embeddings:** `all-MiniLM-L6-v2` (HuggingFace, local, ~90MB, no API key)
- **Vector store:** ChromaDB (local, persisted to disk)
- **LLM:** Llama 3.1 8B via Ollama (local, no API key)

## Pipeline
```
Policy document → chunked → embedded → stored in ChromaDB
Question → embedded → similarity search (top-3 chunks) → threshold check
  → if no relevant match: refuse before calling the LLM
  → if relevant: pass retrieved chunks + question to LLM → grounded JSON answer
```

## Test document
A 20-section mock HR/IT policy handbook (`data/hr_policy.txt`) covering leave, remote 
work, IP assignment, InfoSec, expenses, etc. Deliberately does **not** cover political 
office/parliament or stock trading — used to test retrieval behavior on genuinely 
out-of-scope questions.

## Key findings

### 1. Retrieval alone cannot say "I don't know" — it always returns *something*
Vector similarity search has no built-in relevance floor. Asked about a completely 
unrelated topic (an employee's father being an MP; friends asking about buying company 
stock), it still confidently returned the "closest" chunk — an unrelated IP/Open Source 
clause and an SLA/communications clause, respectively — with no signal that these were 
bad matches. Without an explicit check, a downstream LLM would receive irrelevant context 
labeled as "relevant," which is a more dangerous failure than an obvious retrieval miss, 
because it looks like a normal RAG response.

### 2. Distance thresholds are usable, but must be empirically calibrated, not assumed
Testing 5 questions (2 clearly covered, 1 borderline, 2 clearly not covered) against the 
same document showed a real, usable gap in Chroma's distance scores:

| Question type | Distance range |
|---|---|
| Clearly covered | 0.78 – 0.84 |
| Borderline / adjacent topic | 0.98 |
| Not covered at all | 1.32 – 1.45 |

Thresholds set at **<1.0 = confident, 1.0–1.2 = borderline, >1.2 = no match** based on 
this data. This calibration is specific to this embedding model and this document's 
vocabulary — not a universal constant. A production system would calibrate against a 
larger labeled test set.

### 3. The LLM is a necessary reasoning layer on top of retrieval, not a redundant one
Chroma's retrieval is topic-similarity only — it has no concept of whether a chunk 
actually *answers* the question. On the borderline case ("can I carry forward my sick 
leave"), Chroma retrieved the *Annual Leave* chunk (topically close, but about the wrong 
type of leave). The LLM correctly recognized the mismatch and marked the response 
`"grounded": false` — genuine reasoning beyond what retrieval alone determined.

### 4. Grounding contract needs to be explicit about partial-leak behavior
Initial version of the LLM prompt correctly set `grounded: false` on the sick-leave 
question, but still leaked unrelated retrieved content (the annual-leave text) into the 
`answer` field alongside the refusal message. Fixed by making the refusal text exact and 
mandatory, and explicitly forbidding any other content in `answer` when `grounded` is 
false. Re-tested and verified fixed.

## Architecture decision: threshold check happens in Python, before the LLM call
Rather than relying on the LLM alone to catch irrelevant retrieved context (as in 
finding #3, which worked but only after the fact), a hard distance threshold in code 
skips the LLM call entirely when retrieval confidence is too low. This is both a cost/
latency optimization (no wasted LLM call) and a safety measure — it doesn't depend on 
the LLM behaving well every time.

## Known limitations
- Threshold values are calibrated from only 5 test questions on one document — not 
  statistically robust, would need a larger eval set for production use.
- Chunking still occasionally splits across section boundaries (visible in early tests 
  where two unrelated sections appeared in one chunk); a header-aware or 
  semantic-chunking approach would likely improve this further.
- Local Llama 3.1 8B used for cost-free testing; not yet compared against a larger 
  hosted model (e.g. Claude) for answer quality on the same test set — planned as a 
  follow-up comparison.

## Test results (all 5 questions, final pipeline)

| Question | Distance | Path taken | Result |
|---|---|---|---|
| Paid leave days? | 0.7776 | LLM called | ✅ "28 days", grounded: true |
| Remote work policy? | 0.8427 | LLM called | ✅ Correct excerpt-based answer, grounded: true |
| Sick leave carry-forward? | 0.9781 | LLM called | ✅ Correctly refused despite topically-close chunk, grounded: false |
| Father is an MP? | 1.3241 | Skipped — no LLM call | ✅ Refused pre-LLM, correct |
| Friends ask about stock? | 1.4545 | Skipped — no LLM call | ✅ Refused pre-LLM, correct |