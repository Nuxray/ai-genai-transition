# Invoice Extraction & Validation

## Objective
Extract structured invoice data (header fields + line items) and run business 
validation checks (arithmetic, threshold, date, compliance) for a finance 
automation pipeline, with independently auditable results.

## v1 (initial draft — extraction only, single flat validation field)

**System prompt (abridged — extraction rules only):**
```
Extract header fields (vendor_name, invoice_number, invoice_date, due_date, 
po_number, currency, subtotal, tax_amount, total_amount) and a line_items array.

Validation rules:
- If total_amount > 1000, reimbursement = false
- If invoice_date > current date, reimbursement should not proceed
- If GSTN present, show it, else null and reimbursement = false

[single flat "reimbursement" field in output]
```

**Test input:**
```
Acme Supplies Ltd — Invoice INV-2091
Bill to: Global Tech Staffing, PO# PO-7734
Date: 12/07/2026   Due: 26/07/2026
GSTN : ABCDEFG1025478
Item                  Qty   Unit Price   Total
Office Chairs         10    45.00        450.00
Desk Lamps            20    12.50        250.00
Internet Broadband    10    55.52        550.00
Subtotal: 1250.00
Tax (10%): 70.00
Total Due: USD 1320.00
```

**Output:**
```json
{
  "vendor_name": "Acme Supplies Ltd",
  "invoice_number": "INV-2091",
  "invoice_date": "2026-07-12",
  "due_date": "2026-07-26",
  "po_number": "PO-7734",
  "currency": "USD",
  "subtotal": 1250.00,
  "tax_amount": 70.00,
  "total_amount": 1320.00,
  "reimbursement": false,
  "GSTN": "ABCDEFG1025478",
  "line_items": [
    {"description": "Office Chairs", "quantity": 10, "unit_price": 45.00, "line_total": 450.00},
    {"description": "Desk Lamps", "quantity": 20, "unit_price": 12.50, "line_total": 250.00},
    {"description": "Internet Broadband", "quantity": 10, "unit_price": 55.52, "line_total": 550.00}
  ],
  "extraction_confidence": "high"
}
```

## Findings (v1)

1. **Missed a real arithmetic error.** `Internet Broadband: 10 × 55.52 = 555.20`, but the invoice states `550.00` — the model copied the stated total without checking it. Line-item math validation needed to be added explicitly.

2. **Relied on the model's internal sense of "today," which is unreliable.** An LLM has no live clock; date-validity checks must have the current date injected explicitly as a variable rather than inferred.

3. **Single flat `reimbursement` field lost traceability.** With three rules feeding one boolean, there was no way to tell *which* rule caused a `false` result — a real compliance/audit problem. Needed independent, per-check results with human-readable notes.

## v2 (fixed)

**System prompt:** full independent validation object — `line_item_math_check`, 
`amount_threshold_check`, `date_validity_check`, `gstn_check`, each with `passed` 
+ `note`, plus `overall_reimbursement_eligible` derived from all four. Current date 
passed explicitly as `{current_date}` rather than inferred.

**Test input:** same invoice as v1, with `Current date for validation: 2026-07-15` 
explicitly provided.

**Output:**
```json
{
  "vendor_name": "Acme Supplies Ltd",
  "invoice_number": "INV-2091",
  "invoice_date": "2026-07-12",
  "due_date": "2026-07-26",
  "po_number": "PO-7734",
  "currency": "USD",
  "subtotal": 1250.00,
  "tax_amount": 70.00,
  "total_amount": 1320.00,
  "gstn": "ABCDEFG1025478",
  "line_items": [
    {"description": "Office Chairs", "quantity": 10, "unit_price": 45.00, "line_total": 450.00},
    {"description": "Desk Lamps", "quantity": 20, "unit_price": 12.50, "line_total": 250.00},
    {"description": "Internet Broadband", "quantity": 10, "unit_price": 55.52, "line_total": 550.00}
  ],
  "extraction_confidence": "high",
  "validation": {
    "line_item_math_check": {
      "passed": false,
      "note": "One line item does not match quantity × unit_price within rounding tolerance.",
      "line_item_discrepancies": ["Internet Broadband"]
    },
    "amount_threshold_check": {
      "passed": false,
      "note": "Total amount (1320.00) exceeds 1000; this invoice requires manual approval rather than auto-reimbursement."
    },
    "date_validity_check": {
      "passed": true,
      "note": "Invoice date (2026-07-12) is on or before the current date (2026-07-15)."
    },
    "gstn_check": {
      "passed": true,
      "note": "GSTN value ABCDEFG1025478 was found on the invoice."
    },
    "overall_reimbursement_eligible": false
  }
}
```

## Findings (v2 — verified)

- Line-item math discrepancy correctly caught and named (`Internet Broadband`).
- Each validation check reports independently with a clear, human-readable note — 
  `overall_reimbursement_eligible: false` is now fully explainable from the object alone.
- Explicit date injection removed reliance on the model's internal clock.
- GSTN is preserved as extracted data, decoupled from its own separate pass/fail check.

**Status:** v2 verified and working. This structure is designed to feed directly into 
the Project 2 CrewAI Validator/Exception-Handler agents later — `overall_reimbursement_eligible` 
drives routing, individual `note` fields drive exception messaging back to the vendor.