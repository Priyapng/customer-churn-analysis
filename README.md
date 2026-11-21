# Customer Churn Data Quality & Exploratory Analysis Project

**One Proof Link Repository / Submission Folder**

This repository provides an audit-ready, reproducible data cleaning pipeline, data quality report, exploratory analysis, and executive decision brief for the Customer Churn dataset.

---

## 📁 Repository Contents

| File | Description |
| :--- | :--- |
| [`customer_churn_raw.csv`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/customer_churn_raw.csv) | The untouched source dataset (15 records, 11 columns). |
| [`customer_churn_cleaned.csv`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/customer_churn_cleaned.csv) | Cleaned, typed, normalized, and feature-engineered dataset ready for analysis. |
| [`customer_churn_analysis.xlsx`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/customer_churn_analysis.xlsx) | Professional 5-sheet formatted Excel workbook (Executive Summary, Cleaned Data, Audit Log, Summary Stats, Segment Breakdown). |
| [`customer_churn_analysis.ipynb`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/customer_churn_analysis.ipynb) | Complete Jupyter Notebook with code, data profiling, mathematical checks, statistical tables, and markdown narratives. |
| [`data_dictionary.md`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/data_dictionary.md) | Standardized metadata, business definitions, value domains, and measurement scales for all fields. |
| [`data_quality_report.md`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/data_quality_report.md) | Comprehensive defensible data quality audit, cleaning decisions, exploratory statistics, and executive decision brief. |
| [`clean_and_analyze.py`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/clean_and_analyze.py) | Standalone Python CLI script to reproduce data validation and cleaning end-to-end. |
| [`generate_deliverables.py`](file:///C:/Users/asus/.gemini/antigravity/scratch/customer_churn_analysis/generate_deliverables.py) | Complete Python automation script generating notebook, Excel workbook, and visualizations. |
| `figures/` | High-resolution publication-ready charts (`churn_by_contract.png`, `tickets_vs_tenure_churn.png`, `churn_by_tier_payment.png`). |

---

## 🚀 Quickstart & Reproducibility

To re-run the validation and data cleaning pipeline from the command line:

```bash
python clean_and_analyze.py
```

To re-generate the entire artifact suite including Excel workbooks, charts, and Jupyter notebook:

```bash
python generate_deliverables.py
```

---

## 🎯 Executive Decision Brief Summary

- **Decision Question:** Which customer groups should a fictional subscription team contact first to reduce avoidable churn?
- **Audience:** Customer Success Leadership, Head of Subscription Operations, Retention Outreach Team.
- **Decision:** Prioritize immediate proactive outreach to **Month-to-Month customers who have logged 3 or more support tickets within their first 12 months**.
- **Supporting Metric:** 100% of Month-to-Month customers with $\ge 3$ support tickets churned. Churned customers averaged 4.29 support tickets (vs. 1.00 for retained customers).
- **Uncertainty:** Correlation does not imply causation; ticket volume could reflect acute bugs rather than lack of intent; sample size is $N=15$.
- **Next Measurement:** Launch a 30-day intervention pilot targeting accounts reaching 2+ tickets with concierge onboarding; measure 30-day ticket resolution rate, CSAT, and 60-day renewal rate vs. an uncontacted holdout.
