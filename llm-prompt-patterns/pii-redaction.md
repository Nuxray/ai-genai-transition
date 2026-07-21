# PII Redaction from Support Tickets/Emails

## Objective
Detect and redact personally identifiable information (PII) from support tickets/emails 
while preserving message meaning, with a structured audit log of what was redacted.

## v1 (initial draft)

**System prompt:**
```
You are a PII redaction assistant for internal support tickets.

Your task: identify and redact personally identifiable information (PII) from the ticket text below, while preserving the overall meaning and structure of the message.

Redact the following categories, replacing each with a bracketed placeholder:
- Full names → [NAME]
- Email addresses → [EMAIL]
- Phone numbers → [PHONE]
- Physical addresses → [ADDRESS]
- Employee/Account IDs → [ID]
- Bank account or card numbers → [FINANCIAL_INFO]

Rules:
- Do not redact company names, product names, or general job titles.
- Do not alter any non-PII content.
- If the same PII item appears more than once, redact all instances consistently.

Return your output as JSON with two fields:
- "redacted_text": the ticket text with PII replaced
- "redaction_log": a list of objects, each with "type" and "original_value", for every item redacted

Ticket text:
{ticket_text}
```

**Test input (tabular vendor/salary summary — deliberately includes one PII value, 
the phone number, repeated identically across all 6 rows to test log de-duplication behavior):**
```
Meeting Summary
Date of Discussion: July 14, 2026
Objective: Finalize salary brackets and onboarding logistics for upcoming contracts.

Personnel & Compensation Overview
Prime Solutions Ltd. — John Doe — Senior Developer — +91 98765 4321 — 012 MG Road, Pune — Aug 01, 2026 — $4,500
Prime Solutions Ltd. — Sarah Smith — HR Manager — +91 98765 4321 — 145 FC Road, Pune — Aug 01, 2026 — $3,800
Apex Dynamics — Amit Patel — Lead Contractor — +91 98765 4321 — 2101 Senapati Bapat Rd, Pune — Aug 10, 2026 — $5,200
Apex Dynamics — Priya Sharma — Tech Vendor — +91 98765 4321 — 377 Prabhat Rd, Pune — Aug 10, 2026 — $4,900
Global Tech Staffing — Mark Taylor — Site Supervisor — +91 98765 4321 — 433 Baner Road, Pune — Sep 01, 2026 — $2,900
Global Tech Staffing — Anjali Verma — Contract Manager — +91 98765 4321 — 588 Aundh, Pune — Sep 01, 2026 — $3,500

Action Items & Next Steps
Contracts: HR to dispatch finalized offer letters to all listed vendors by July 20, 2026.
Onboarding: Vendor managers to submit required compliance paperwork for John Doe and Sarah Smith.
Budget: Finance to adjust baseline project budgets according to the finalized salary figures.
```

**Output:**
```json
{
  "redacted_text": "...[all 6 names → [NAME], phone → [PHONE], addresses → [ADDRESS]]...",
  "redaction_log": [
    {"type": "NAME", "original_value": "John Doe"},
    {"type": "NAME", "original_value": "Sarah Smith"},
    {"type": "NAME", "original_value": "Amit Patel"},
    {"type": "NAME", "original_value": "Priya Sharma"},
    {"type": "NAME", "original_value": "Mark Taylor"},
    {"type": "NAME", "original_value": "Anjali Verma"},
    {"type": "PHONE", "original_value": "+91 98765 4321"},
    {"type": "ADDRESS", "original_value": "012 MG Road, Pune"},
    {"type": "ADDRESS", "original_value": "145 FC Road, Pune"},
    {"type": "ADDRESS", "original_value": "2101 Senapati Bapat Rd, Pune"},
    {"type": "ADDRESS", "original_value": "377 Prabhat Rd, Pune"},
    {"type": "ADDRESS", "original_value": "433 Baner Road, Pune"},
    {"type": "ADDRESS", "original_value": "588 Aundh, Pune"}
  ]
}
```

## Findings

1. **Correctly preserved non-PII business data** — salary figures and company names were left untouched, exactly per spec.

2. **Correctly redacted and de-duplicated a repeated PII value.** All 6 rows shared an identical phone number (a copy-paste artifact in the test data). The model logged it once rather than 6 times — consistent with the "redact all instances consistently" instruction, but this surfaced a real ambiguity: the prompt never specified whether `redaction_log` should count *unique values* or *every occurrence*. For audit purposes (proving how many times PII appeared, not just that it appeared), per-occurrence logging is more useful.

3. **Structure loss:** the original text was semi-tabular; `redacted_text` came back as a flattened paragraph. Table/structure-aware redaction is a known gap, tracked as future work.

## v2 refinement

Add to the rules section:
```
For the redaction_log, include one entry per occurrence (not just unique values) — 
if the same PII item appears multiple times, log it each time it appears, so the 
count of log entries matches the count of redactions made in redacted_text.
```

**Status:** v2 not yet re-tested. Next step is re-running with a test input containing 
genuinely varied repeated values (not identical across all rows) to properly validate 
per-occurrence logging, and testing structure-preserving redaction for tabular input.