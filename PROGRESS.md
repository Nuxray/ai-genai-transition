# AI/GenAI Delivery Role — Progress Tracker (v2)
Started: 07/07/2026  |  Rebuilt: 02/09/2026  |  Target completion: ____________

Rebuilt to reflect: (1) work already completed and shipped, (2) a proper Python
foundations pass, (3) a much deeper CrewAI curriculum matching your company's stack,
and (4) required/recommended Claude training. Nothing below is theoretical —
every week ends in a GitHub-committed artifact, same discipline as before.

---

## ✅ Already completed (don't redo — recap only)

- [x] **Week 1 — Prompt Engineering.** Repo: `llm-prompt-patterns`. 3 fully-tested,
  documented prompt patterns (PII redaction, invoice extraction+validation, HR
  policy Q&A), each with v1→v2 iteration and real findings.
- [x] **Week 2 — RAG.** Repo: `hr-policy-rag`. Local ChromaDB + Ollama pipeline,
  threshold-based relevance guardrail, documented findings on retrieval's inability
  to say "I don't know," and LLM-as-reasoning-layer-on-retrieval.
- [x] **Bonus deliverable — Assessment Document Extraction.** Repo/folder:
  `assessment-doc-extraction`. Multi-format (Excel/PDF/Word) extraction pipeline
  solving a real production problem (HRSS assessment automation). Found and fixed
  a genuine date-ambiguity bug, a type-inconsistency bug, and a JSON-parsing
  robustness gap. Concurrency test in progress.

These three are strong, real portfolio pieces — keep them as-is, just make sure
each has an up-to-date README before you move to the internal pitch stage later.

---

## Week 0 — Python Foundations for AI Engineering
*New — added because CrewAI, agent tooling, and API-based work all assume this level
of Python fluency. If a topic already feels solid from your existing scripting
work, skim and check it off rather than doing it start to finish.*

- [X] Python Setup: `venv` & virtual environments (you've done this manually
  already via Poetry — just formalize the underlying concept)
- [X] Python Basics: types, control flow, functions
- [X] Python Classes & OOP basics
- [X] `uv` package manager (CrewAI's preferred installer — faster than Poetry/pip,
  worth learning since CrewAI docs/CLI assume it)
- [X] Env vars & API keys with `python-dotenv`
- [X] Calling REST APIs with `requests`
- [X] Async Python (`asyncio`) basics
- [X] Type hints & Pydantic models *(CrewAI uses Pydantic heavily for structured
  agent outputs — don't skip this one)*
- [X] **Deliverable:** a short `python-foundations` notes repo or folder — doesn't
  need to be elaborate, just 5-10 small working code snippets proving each concept,
  committed to GitHub. This becomes a fast personal reference later.

---

## Week 3 — CrewAI Foundations
*Rebuilt from your old Week 3-4. Split into three progressive weeks (3, 4, 5) since
the topic list is now much deeper than the original plan.*

- [Progress Bar] What Is CrewAI? Introduction
- [ ] Version awareness: changelog & upgrading (CrewAI moves fast — check current
  version against what tutorials assume)
- [ ] CrewAI installation (via `uv`)
- [ ] Agents concept
- [ ] Agent capabilities: Tools, MCPs, Apps, Skills, Knowledge
- [ ] Tasks concept
- [ ] Crews concept
- [ ] Quickstart: your first CrewAI Flow
- [ ] Guide: Build your first Crew (JSON-first)
- [ ] CrewAI CLI (`create` / `run` / `--classic`)
- [ ] Processes: Sequential vs Hierarchical
- [ ] Task guardrails & validation
- [ ] LLM configuration (Claude, OpenAI, Gemini, Azure, Bedrock) — configure at
  least Claude + one local/Ollama option since that's your free dev path
- [ ] Tools overview (40+ built-in tools)
- [ ] Create custom tools
- [ ] **Deliverable:** rebuild the invoice-crew skeleton (already environment-tested
  with Ollama earlier) as your actual first working Crew — Extractor agent only for
  now, using a custom tool that reuses your assessment-doc-extraction extractors.

---

## Week 4 — CrewAI Flows & Intermediate Patterns

- [ ] Flows concept (`@start` / `@listen` / `@router`)
- [ ] Guide: Build your first Flow
- [ ] Conversational Flows (multi-turn chat apps)
- [ ] Async kickoff & fan-out over a list *(directly relevant — this is how you'd
  process a batch of tickets/attachments in parallel, connects to the concurrency
  work you just did manually)*
- [ ] Memory (short-term / long-term / entity)
- [ ] Knowledge & RAG sources *(connects directly to your Week 2 RAG project — CrewAI
  has built-in RAG source support, worth comparing to your manual ChromaDB build)*
- [ ] Mastering Flow state management
- [ ] Collaboration & delegation (multi-agent handoff patterns)
- [ ] MCP servers as tools
- [ ] Human-in-the-loop workflows *(important for your finance/HR use cases —
  low-confidence extractions should route to a human, same pattern you already
  built manually)*
- [ ] Files & multimodal agents
- [ ] **Deliverable — Project 2: Finance Invoice Processing Crew (full version)**
  - [ ] Agent 1: Extractor (reuse your multi-format extraction work)
  - [ ] Agent 2: Validator (cross-check vs mock SQL Server ERP data)
  - [ ] Agent 3: Exception Handler (flags mismatches, drafts email/ticket)
  - [ ] Agent 4: Approver-router (threshold-based routing)
  - [ ] Orchestrate with CrewAI Flows (not just sequential Crew)
  - [ ] Add audit logging for every step
  - [ ] Push to GitHub with README + demo GIF

---

## Week 5 — CrewAI Advanced & Production Readiness

- [ ] Evaluating use cases: Crews vs Flows (when to use which)
- [ ] Crafting effective agents
- [ ] Reasoning & planning
- [ ] Testing your Crew (`crew.test`)
- [ ] Training agents with feedback
- [ ] Observability & tracing
- [ ] MCP security considerations
- [ ] Production architecture (Flow-first mindset)
- [ ] Execution hooks (`@on`) & event listeners
- [ ] Checkpointing & failure recovery
- [ ] CrewAI skills for coding agents (Claude Code / Cursor)
- [ ] Deployment & the AMP REST contract
- [ ] DeepLearning.AI "Design, Develop, and Deploy Multi-Agent Systems with CrewAI"
  (earn certificate — this is the official course, high value for your resume)
- [ ] **CAPSTONE:** Build & demo your own Crew — use this to harden Project 2 into
  something production-shaped: checkpointing, observability/tracing, and a tested
  failure-recovery path, not just a happy-path demo.

*Optional, at your own pace once the above is solid:*
- [ ] "Practical Multi AI Agents and Advanced Use Cases with crewAI" (supplementary)
- [ ] CrewAI Full Course (playlist) — Crew Basic, Crew Advanced modules for anything
  not already covered above

---

## Week 6 — Kore.ai
*Unchanged from original plan.*

- [ ] Kore.ai Academy — "XO Platform: End-to-End (Basic)" learning path
- [ ] Kore.ai Academy — intermediate/advanced NLP + dialog tasks path
- [ ] Understand: intent/entity design, dialog tasks, webhook/REST integration
- [ ] Build a demo virtual assistant (dialog flows + backend webhook)
- [ ] **Deliverable:** design doc + screen-recorded demo (bot JSON export +
  integration code to GitHub)

---

## Week 7 — LLMOps, Evaluation, Guardrails & Claude Platform Depth

- [ ] Prompt versioning, eval harnesses, rate limiting, PII guardrails,
  human-in-the-loop (concepts)
- [ ] Cost estimation per token, latency tradeoffs
- [ ] Add evaluation + logging layer to Project 1 (HR RAG) and Project 2 (Invoice Crew)
- [ ] Complete required Claude training (see checklist below)

---

## Week 8 — Flagship Project + Portfolio Polish

- [ ] **Deliverable — Project 3: RPA-to-Agentic Migration Framework**
  - [ ] Architecture diagram (draw.io/Excalidraw): RPA-only vs agentic
  - [ ] Build demo: LLM agent decides when to trigger deterministic RPA/API/UI steps
  - [ ] Add Kore.ai chat front-end that triggers CrewAI backend
  - [ ] Comparison table: cost, latency, accuracy, failure modes
  - [ ] One-page ROI narrative
  - [ ] Push to GitHub with full README + architecture diagram
- [ ] Write "problem → approach → result" README for all 4 projects (including the
  assessment-doc-extraction bonus deliverable)
- [ ] Record 2–3 min demo video/Loom for each project
- [ ] Build internal pitch deck for leadership (reuse ROI narrative + comparison table)

---

## Practical Project Map — learn-by-building, not learn-then-build

*Training alone won't move you from BAU to delivery — what convinces a hiring
manager is evidence you can ship. Every advanced CrewAI topic below gets a small,
real exercise attached, so nothing stays theoretical. Most of these are 1-3 hour
add-ons to your existing Invoice Crew / HR RAG projects, not separate builds —
BAU-to-delivery reviewers want to see depth on a few things, not 15 shallow demos.*

| Topic (from Week 4-5 training) | Practical exercise | Where it lives |
|---|---|---|
| Async kickoff & fan-out over a list | Batch-process all 5 assessment-doc-extraction sample files through a CrewAI Flow instead of your manual `ThreadPoolExecutor` script — compare the two approaches in your README | `assessment-doc-extraction` |
| Knowledge & RAG sources | Rebuild your Week 2 HR Policy RAG using CrewAI's built-in Knowledge source instead of manual ChromaDB — document what CrewAI handles for you vs what you had to build by hand | `hr-policy-rag` (new branch/variant) |
| Human-in-the-loop workflows | Add a real HITL step to Invoice Crew: any invoice below a confidence/threshold pauses the Flow and waits for a manual "approve/reject" input before continuing | `invoice-crew` |
| Task guardrails & validation | Add CrewAI-native guardrails to the Extractor agent enforcing your existing rules (score/total_score must be numeric, employee_number must match your 9-digit pattern) instead of your manual Python validation | `assessment-doc-extraction` |
| Memory (short-term/long-term/entity) | Extend the HR RAG assistant to remember prior questions in a session (e.g., "what about sick leave?" after asking about annual leave) — a real user-facing improvement over Week 2's one-shot Q&A | `hr-policy-rag` |
| Testing your Crew (`crew.test`) | Write a small test suite for Invoice Crew using your 5 assessment sample files as fixtures (you already have known-correct expected outputs from earlier testing) | `invoice-crew` |
| Observability & tracing | Add tracing to Invoice Crew and capture one real trace showing the full agent decision path for a flagged exception — screenshot/export it for your portfolio README | `invoice-crew` |
| Checkpointing & failure recovery | Kill a running Flow mid-execution on purpose, restart it, confirm it resumes rather than reprocessing from scratch — document the before/after | `invoice-crew` |
| MCP servers as tools | Wire one real MCP server (e.g., a filesystem or GitHub MCP) into a Crew as a tool — small standalone demo, doesn't need to touch existing projects | new: `mcp-tool-demo` |
| Reasoning & planning | Add a planning step to the Approver-router agent so it explains *why* it routed an invoice a certain way, not just the routing decision — direct upgrade to your existing audit-log finding from Week 1 | `invoice-crew` |

**How to use this table:** as you go through each Week 4-5 training topic, do the
matching exercise the same day if possible — small, immediate, hands-on, same
discipline as Weeks 1-2. Check items off here as you complete them; they feed
directly into hardening Project 2 for the capstone.

- [ ] Async fan-out exercise
- [ ] Knowledge/RAG source exercise
- [ ] Human-in-the-loop exercise
- [ ] Task guardrails exercise
- [ ] Memory exercise
- [ ] crew.test exercise
- [ ] Observability/tracing exercise
- [ ] Checkpointing exercise
- [ ] MCP tool demo
- [ ] Reasoning/planning exercise

---

## BAU → Delivery: what to actually show your leadership

*A BAU role gets judged on "did the automation run correctly today." A delivery
role gets judged on "can this person architect and ship a new solution." Your
portfolio needs to visibly demonstrate the second, not just the first.*

- [ ] **Before/after story:** for at least one real BAU process you already
  automate (assessment doc processing is the natural one — you already have this
  built), write a one-pager: "here's the RPA-only version, here's the failure
  rate/manual effort it required, here's the agentic version, here's what improved
  and what the new failure modes are." Brutal honesty about new failure modes
  (e.g., LLM type-inconsistency bug you found) makes this more credible, not less.
- [ ] **Cost/latency/accuracy comparison table** — you already have real data from
  the concurrency test (sequential vs parallel timing) and the local-Llama testing.
  Turn that into a simple table for non-technical leadership: "local/free vs
  hosted API, tradeoffs in speed/cost/accuracy."
- [ ] **A short recorded walkthrough** (Loom, 3-5 min) of Invoice Crew actually
  running end-to-end on realistic data — leadership skims READMEs but watches videos.
- [ ] **Position the ask explicitly:** don't just show projects and hope someone
  notices. Bring the before/after one-pager and the demo video to a direct
  conversation: "I've been prototyping this outside of my BAU work — here's what
  it can do, here's what I'd need (time, access, a pilot process) to take this
  further as part of a delivery engagement."

---

## Claude Platform Training Checklist

**Required — complete all of these:**
- [ ] Claude 101
- [ ] Claude Opus Overview
- [ ] Claude Sonnet Overview
- [ ] Claude Haiku Overview
- [ ] Claude Use Cases
- [ ] What Are Skills
- [ ] Intro to Artifacts
- [ ] Intro to Projects
- [ ] Use Skills in Claude
- [ ] Introduction to Claude Cowork

**Recommended — pick based on relevance to your role (suggested subset given your
Finance/HR delivery focus and Solutions Architect target: prioritize the starred ones):**
- [ ] ⭐ Getting the Most Out of Sonnet 4.5
- [ ] Get the Most from Opus 4.6
- [ ] ⭐ Claude for Product Management *(useful framing for Solutions Architect
  conversations with leadership)*
- [ ] ⭐ Using Research
- [ ] Connect Your Tools to Claude
- [ ] ⭐ Batch Processing *(relevant — this is the hosted-API equivalent of the
  concurrency pattern you just built manually)*
- [ ] ⭐ Prompt Engineering Interactive Tutorial
- [ ] ⭐ Claude Prompting Best Practices
- [ ] IDE Integrations (Claude Code)
- [ ] ⭐ Real World Prompting
- [ ] Prompt Evaluations Course
- [ ] Building Evals Cookbook
- [ ] Develop Tests
- [ ] How to Create Custom Skills
- [ ] ⭐ Tool Use Course *(directly relevant to CrewAI tool-calling work)*
- [ ] ⭐ MCP: Connect Local Servers *(relevant — CrewAI's MCP-as-tools topic in Week 4)*
- [ ] MCP Servers Repository

**Optional — skip unless curious or a specific need comes up:**
- [ ] Claude for Engineering
- [ ] Claude Code in Action
- [ ] Build with Claude
- [ ] Messages API
- [ ] Using the GitHub Integration
- [ ] Computer Use Tool

---

## Certifications Checklist
- [ ] DeepLearning.AI CrewAI course certificate
- [ ] Kore.ai Academy XO Platform path completion
- [ ] DeepLearning.AI LangChain courses *(already done — Week 1-2)*
- [ ] (Optional) Microsoft Azure AI Fundamentals (AI-900)

---

## Internal Positioning Checklist
- [ ] Share flagship project (Project 3) with manager before role is formally posted
- [ ] Reframe project outcomes in business terms (cost savings, exception-handling
  rate, audit improvement) — you already have real numbers/findings from the
  assessment-doc-extraction bonus project, use them
- [ ] Volunteer for any internal CrewAI/Kore.ai pilot
- [ ] Draft one-page internal case study styled as a client deliverable

---

## Notes / Adjustments Log

- Week 1: Delivered 3 fully-tested prompt patterns instead of 10-15 shallow
  templates. Prioritized depth over breadth. Key finding: models can produce
  outputs that *look* correct/grounded while subtly violating instructions.
- Week 2: Completed "Chat with Your Data" course + built full RAG pipeline.
  Key finding: retrieval alone can't say "I don't know" — needs explicit
  threshold guardrails; LLM is a necessary reasoning layer on top of retrieval,
  not redundant with it.
- Bonus (pre-Week-3 detour): Built a real production-relevant deliverable
  (multi-format assessment doc extraction for HRSS automation). Found and fixed
  a genuine date-format ambiguity bug and a type-consistency bug — both are
  strong "found it before it broke something" stories for interviews. Confirmed
  the general principle: never trust LLM output formatting/typing purely via
  instructions — enforce with code-level validation regardless of how explicit
  the prompt is.
- 02/09/2026: Lost momentum after the bonus project due to unforeseen
  circumstances; company is now formally pushing AI training, which raised
  urgency. Rebuilt plan (this version) with a Python foundations week and a much
  deeper CrewAI curriculum, since original Week 3-4 scope was too shallow given
  what's now expected. Existing Week 1-2 work and the bonus project remain valid
  and don't need to be redone.
-
