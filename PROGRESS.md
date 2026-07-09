# AI/GenAI Delivery Role — Progress Tracker
Started: 07/07/2026  |  Target completion: ____________

Tip: open this in VS Code / Obsidian / any markdown editor — the `- [ ]` boxes are clickable checkboxes. Commit this file to your portfolio repo and update it weekly.

---

## Week 1 — LLM & Prompt Engineering Foundations
- [x] Anthropic Prompt Engineering docs (read + try examples)
- [In-progress] DeepLearning.AI "ChatGPT Prompt Engineering for Developers"
- [In-progress] DeepLearning.AI "LangChain for LLM Application Development"
- [In-progress] Understand: tokens, context window, temperature, system vs user prompts
- [In-progress] Understand: few-shot prompting, structured/JSON output, function/tool calling
- [ ] **Deliverable:** Create GitHub repo `llm-prompt-patterns`
- [ ] Add 10–15 reusable prompt templates (invoice extraction, PII redaction, ticket classification, HR Q&A)
- [ ] Push repo + write README

---

## Week 2 — RAG (Retrieval-Augmented Generation)
- [ ] DeepLearning.AI "LangChain: Chat with Your Data"
- [ ] Understand: embeddings, vector DBs, chunking strategies, retrieval evaluation
- [ ] Set up ChromaDB or FAISS locally
- [ ] **Deliverable — Project 1: HR Policy & Payroll Query Assistant**
  - [ ] Gather/anonymize sample HR policy docs
  - [ ] Build chunk → embed → store pipeline
  - [ ] Build retrieval + LLM answer with citations
  - [ ] Add PII/role-access guardrail agent
  - [ ] Push to GitHub with README + demo GIF

---

## Week 3–4 — Agentic Systems with CrewAI
- [EnvironmentReady] DeepLearning.AI "Design, Develop, and Deploy Multi-Agent Systems with CrewAI" (earn certificate)
- [ ] DeepLearning.AI "Practical Multi AI Agents and Advanced Use Cases with crewAI"
- [ ] Understand: agents, tasks, crews, memory, tools, guardrails, Flows
- [ ] Understand: observability/traces, LLM-as-a-Judge evaluation
- [ ] **Deliverable — Project 2: Finance Invoice Processing Crew**
  - [ ] Agent 1: Extractor (PDF/email → structured JSON)
  - [ ] Agent 2: Validator (cross-check vs mock SQL Server ERP data)
  - [ ] Agent 3: Exception Handler (flags mismatches, drafts email/ticket)
  - [ ] Agent 4: Approver-router (threshold-based routing)
  - [ ] Orchestrate with CrewAI Flows
  - [ ] Add audit logging for every step
  - [ ] Push to GitHub with README + demo GIF

---

## Week 5 — Kore.ai
- [ ] Kore.ai Academy — "XO Platform: End-to-End (Basic)" learning path
- [ ] Kore.ai Academy — intermediate/advanced NLP + dialog tasks path
- [ ] Understand: intent/entity design, dialog tasks, webhook/REST integration
- [ ] Build a demo virtual assistant (dialog flows + backend webhook)
- [ ] **Deliverable:** Design doc + screen-recorded demo (bot JSON export + integration code to GitHub)

---

## Week 6 — LLMOps, Evaluation, Guardrails, Cost/Latency
- [ ] Learn: prompt versioning, eval harnesses, rate limiting, PII guardrails, human-in-the-loop
- [ ] Learn: cost estimation per token, latency tradeoffs
- [ ] Add evaluation + logging layer to Project 1
- [ ] Add evaluation + logging layer to Project 2

---

## Week 7–8 — Flagship Project + Portfolio Polish
- [ ] **Deliverable — Project 3: RPA-to-Agentic Migration Framework**
  - [ ] Architecture diagram (draw.io/Excalidraw): RPA-only vs agentic
  - [ ] Build demo: LLM agent decides when to trigger deterministic RPA/API/UI steps
  - [ ] Add Kore.ai chat front-end that triggers CrewAI backend
  - [ ] Comparison table: cost, latency, accuracy, failure modes
  - [ ] One-page ROI narrative
  - [ ] Push to GitHub with full README + architecture diagram
- [ ] Write "problem → approach → result" README for all 3 projects
- [ ] Record 2–3 min demo video/Loom for each project
- [ ] Build internal pitch deck for leadership (reuse ROI narrative + comparison table)

---

## Certifications Checklist
- [ ] DeepLearning.AI CrewAI course certificate
- [ ] Kore.ai Academy XO Platform path completion
- [ ] DeepLearning.AI LangChain courses
- [ ] (Optional) Microsoft Azure AI Fundamentals (AI-900)

---

## Internal Positioning Checklist
- [ ] Share flagship project (Project 3) with manager before role is formally posted
- [ ] Reframe project outcomes in business terms (cost savings, exception-handling rate, audit improvement)
- [ ] Volunteer for any internal CrewAI/Kore.ai pilot
- [ ] Draft one-page internal case study styled as a client deliverable

---

## Notes / Adjustments Log
_(use this space to note what worked, what to swap, manager feedback, etc.)_

-
-
-
