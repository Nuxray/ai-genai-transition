# LLM Prompt Patterns

A collection of tested, production-oriented prompt patterns built from real Finance 
and HR automation use cases, as part of a structured transition from RPA/Automation 
Engineering into AI/GenAI delivery roles.

Each pattern is documented with its full iteration history — not just a final polished 
prompt, but the failures found along the way and the fixes applied. The goal is to 
demonstrate testing discipline, not just prompt-writing.

## Background

I'm an Automation Engineer (AutomationEdge, Python, JavaScript, REST/SOAP APIs, SQL 
Server) with ~5 years of experience in Finance and HR process automation. This repo is 
the first deliverable in a self-directed transition toward AI/GenAI delivery roles, 
starting with prompt engineering fundamentals before moving into RAG and multi-agent 
systems (CrewAI) in later projects.

## Patterns in this repo

| Pattern | Use case | Key finding |
|---|---|---|
| [`pii-redaction.md`](./prompts/pii-redaction.md) | Redact PII from support tickets/emails while preserving structure, with an audit log | Redaction log needed per-occurrence logging (not just unique values) for real audit trails |
| [`invoice-extraction-validation.md`](./prompts/invoice-extraction-validation.md) | Extract structured invoice data + run finance validation rules (arithmetic, threshold, date, compliance) | A flat single `reimbursement` boolean hid *why* an invoice failed; rebuilt as independent, auditable per-check results. Also caught a real line-item arithmetic error the v1 prompt missed. |
| [`hr-policy-qa.md`](./prompts/hr-policy-qa.md) | Answer employee questions strictly grounded in a policy document, with section citation | Found a subtle failure mode: the model synthesized two unrelated policy sections into an answer that *looked* grounded but violated the strict-grounding rule — a more dangerous failure than an obvious hallucination |

## What this repo demonstrates

- **Grounding discipline** — testing whether models stick to provided source material 
  rather than filling gaps with plausible-sounding inference (HR Q&A)
- **Business rule validation on top of extraction** — not just pulling data out of 
  documents, but checking it against real operational rules (invoice processing)
- **Audit-first output design** — structuring outputs so every automated decision is 
  traceable to a specific, human-readable reason, which matters for Finance/HR/compliance 
  contexts specifically
- **Adversarial/edge-case testing** — deliberately messy inputs (duplicate section 
  numbers, identical repeated PII values, questions adjacent to but not covered by policy) 
  rather than only testing the happy path

## Structure

```
llm-prompt-patterns/
├── README.md
└── prompts/
    ├── pii-redaction.md
    ├── invoice-extraction-validation.md
    └── hr-policy-qa.md
```

Each pattern file follows the same format: objective → v1 prompt + test → findings → 
v2 refinement (+ re-test where completed).

## Tooling

All patterns tested interactively against Claude (claude.ai, free tier). No paid API 
usage was required for this stage — later projects in this transition plan (RAG, 
CrewAI multi-agent systems) use free/open-source tooling: Ollama for local LLM inference, 
ChromaDB/FAISS for vector storage, and CrewAI for agent orchestration.

## Part of a larger portfolio

This is the first of three planned projects:
1. **This repo** — prompt engineering foundations
2. [HR Policy RAG Assistant] — retrieval-augmented Q&A over real policy documents
3. [Finance Invoice Processing Crew](../invoice-crew) — multi-agent CrewAI system for 
   automated invoice extraction, validation, and exception routing
4. **Flagship:** RPA-to-Agentic Migration Framework — reference architecture for 
   evolving existing RPA automation into agentic, LLM-augmented workflows

Full roadmap and progress tracker: [`PROGRESS.md`](../../PROGRESS.md)