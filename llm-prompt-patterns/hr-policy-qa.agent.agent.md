# HR Policy Q&A

## Objective
Answer employee questions strictly grounded in a provided HR policy document — 
no outside knowledge, no fabricated policy, with section-level citation for auditability.

## v1 (initial draft)

**System prompt:**
```
You are an HR policy assistant. You answer employee questions strictly based on the policy document provided below. You do not use any outside knowledge about HR policy, labor law, or common company practices.

Policy document:
{policy_document}

Rules:
- Answer only using information explicitly present in the policy document above.
- If the answer is not covered in the document, respond: "This isn't covered in the policy document provided. Please check with HR directly." Do not guess or infer beyond what's written.
- When you do answer, cite the specific section or clause title you drew the answer from.
- Keep answers concise and factual — do not add caveats, opinions, or generic HR advice not present in the source document.
- If a question is ambiguous or could relate to multiple sections, ask a clarifying question instead of guessing which one applies.

Return your output as JSON:
{
  "answer": "",
  "source_section": "",
  "grounded": true
}

If the question cannot be answered from the document, set "source_section" to null and "grounded" to false.

Employee question:
{employee_question}
```

**Test document (deliberately messy — contains a duplicate "Section 4" to test citation robustness):**
```
SECTION 1: Confidentiality agreements should be signed by everyone in the company and company's details could not be shared with anyone.
SECTION 2: SALARY DISBURSEMENT — 2.1 Standard Pay Cycle: Salaries are processed and credited on the 1st day of every month. 2.2 Weekend and Holiday Adjustments: If the 1st of the month falls on a Saturday or Sunday, payroll processes on the next business day (Monday). Public holidays falling on the 1st of the month will follow the same next-business-day rule.
SECTION 3: POLITICAL ACTIVITY & PUBLIC OFFICE — 3.1 Strict Political Neutrality: Employees must not engage in any political activities during working hours. Company resources, email accounts, and premises cannot be used for political campaigning. 3.2 Restriction on Public Office: Employees are strictly prohibited from holding office as a Member of Parliament (MP). Acceptance of any parliamentary seat requires immediate resignation from the company.
SECTION 4: COMPANY STOCK PURCHASE ELIGIBILITY — 4.1 Service Period Requirement: Employees are eligible to purchase equity or stock options only after completing 5 years of continuous service. 4.2 Vesting and Compliance: Stock allocations remain subject to standard board approvals upon reaching the 5-year milestone. All trades must comply with insider trading regulations and company blackout periods.
SECTION 4 (duplicate numbering): Paid Leave — Employees are entitled to 18 days of paid leave per calendar year, accrued monthly. Unused leave up to 5 days may be carried forward to the next year. Leave requests must be submitted at least 3 working days in advance via the HR portal.
SECTION 5: Sick Leave — Employees may take up to 10 days of paid sick leave per year. A medical certificate is required for sick leave exceeding 2 consecutive days.
```

**Test questions and results:**

| # | Question | Result |
|---|---|---|
| 1 | How many paid leave days do I get per year? | ✅ Correctly grounded, cited "Paid Leave" by name (worked around duplicate section numbering implicitly) |
| 2 | What's the company policy on remote work? | ✅ Correctly declined — not covered |
| 3 | Can I carry forward my sick leave to next year? | ✅ Correctly declined — did not assume the paid-leave carry-forward rule applied to sick leave |
| 4 | My father is a Member of Parliament — can I work for your company? | ⚠️ Declined as "not covered." Technically correct (policy restricts the *employee*, not relatives) but arguably over-conservative / unhelpful |
| 5 | My friends are asking about company stock status and whether they should buy it | ❌ Marked `grounded: true` while synthesizing two unrelated sections (Confidentiality + Insider Trading) into a novel answer, instead of declining as out-of-scope |

## Findings

1. **Duplicate section numbering breaks reliable citation.** The source document had two "Section 4" headers. The model worked around it by citing a section by descriptive name rather than number, but this was implicit, not something the prompt instructed. Fix: source documents need unique section IDs in production; don't rely on the model to self-correct messy numbering.

2. **Literal grounding vs. helpful scope-reading is a real design tradeoff, not a bug (Q4).** The model refused to answer a question about a third party (employee's father) because the policy only addresses the employee directly. This is defensible strict-literalism, but may read as unhelpfully evasive. Depending on risk tolerance, a refinement rule can allow the assistant to clarify *what the policy does and doesn't cover* without inferring new rules.

3. **Most important finding: multi-section synthesis can produce answers that look grounded but violate the grounding contract (Q5).** Given a question outside the policy's scope, the model combined two unrelated sections (Confidentiality + Insider Trading) to construct a response, and self-reported `grounded: true`. This is a subtle failure mode — the answer *sounds* appropriately cautious, which makes it easy to miss in review, but it's technically an inference the prompt explicitly prohibited. This is a more dangerous failure than an obvious hallucination, because it's harder to catch downstream.

## v2 refinement (proposed, not yet tested)

Add to the rules section:
```
- If a question asks about something adjacent to a policy clause (e.g., about a third party rather than the employee), you may clarify what the policy does and does not cover, as long as you do not infer any new rule not stated in the text.
- Do not combine multiple unrelated sections to construct an answer to a question that isn't directly addressed by any single section. If a question isn't directly covered by one clearly relevant section, treat it as not covered.
```

**Next step:** re-run the same 5 questions against v2 to confirm Q5 now correctly declines instead of synthesizing across sections, and check whether Q4's answer becomes more useful without violating grounding. Not yet tested — tracked as a follow-up.