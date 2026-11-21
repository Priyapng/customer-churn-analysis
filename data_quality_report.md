# Data Quality and Exploratory Analysis Report: Customer Churn Audit

## 1. Executive Summary & Decision Brief

### Strategic Question
> **Decision Question:** *Which customer groups should a fictional subscription team contact first to reduce avoidable churn?*

### Governed Decision Framework
- **Audience:** Head of Customer Success, Subscription Operations Lead, and Retention Outreach Specialists.
- **Decision:** Prioritize immediate proactive outreach (phone and targeted email) to **Month-to-Month customers who have logged 3 or more support tickets and have a tenure under 12 months**.
- **Supporting Metric:**
  - In the audited sample, **100% of Month-to-Month customers (7 out of 7) churned**, whereas 0% of Annual or Biennial contract customers churned.
  - Churned customers logged an average of **4.29 support tickets** in the prior 90 days (range: 3 to 6 tickets), compared to an average of **1.00 ticket** for retained customers (range: 0 to 2 tickets) — a **4.3x escalation**.
  - 100% of customers with $\ge 3$ support tickets churned, and 100% of customers with tenure $\le 14$ months churned.
- **Uncertainty & Governance Guardrails:**
  - *Correlation does not prove causation:* High support ticket volume may reflect acute product onboarding defects, unresolved billing bugs, or inadequate self-service documentation rather than poor customer intent.
  - *Sample size limitation:* $N=15$ represents an initial synthetic audit cohort. While the separation is 100% distinct in this sample, statistical generalizeability requires continuous observation across larger customer volumes.
  - *Survivorship & censoring:* Customers with longer tenures (e.g., 24–48 months) have survived early hazards; early-tenure drop-offs represent early lifecycle friction.
- **Next Measurement & Operational Follow-Up:**
  - Launch a 30-day intervention pilot: Trigger an automated concierge outreach call within 24 hours whenever any Month-to-Month customer logs their second ($2^{\text{nd}}$) support ticket within their first 90 days.
  - Measure 30-day first-contact resolution (FCR), Customer Satisfaction (CSAT), and 60-day cohort renewal rate compared against an uncontacted control holdout group.

---

## 2. Dataset Profiling & Inventory

The raw dataset contains 15 synthetic customer subscription records across 11 raw fields.

| Column Name | Raw Field Name | Inferred Type | Python Data Type | Non-Null Count | Missing (%) | Unique Count | Value Range / Categories |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `customer_id` | `CustomerID` | Text / Identifier | `object` (`str`) | 15 / 15 | 0.0% | 15 | `CUST-1001` to `CUST-1015` |
| `gender` | `Gender` | Categorical | `object` (`str`) | 15 / 15 | 0.0% | 2 | `Female` (8), `Male` (7) |
| `age` | `Age` | Discrete Numeric | `int64` | 15 / 15 | 0.0% | 15 | 23 to 60 years |
| `tenure_months` | `TenureMonths` | Discrete Numeric | `int64` | 15 / 15 | 0.0% | 14 | 2 to 48 months |
| `subscription_type` | `SubscriptionType` | Categorical | `object` (`str`) | 15 / 15 | 0.0% | 3 | `Basic` (7), `Pro` (4), `Enterprise` (4) |
| `monthly_charge` | `MonthlyCharges` | Continuous Numeric | `float64` | 15 / 15 | 0.0% | 3 | ₹49.99, ₹79.99, ₹149.99 |
| `total_charges` | `TotalCharges` | Continuous Numeric | `float64` | 15 / 15 | 0.0% | 15 | ₹99.98 to ₹7,199.52 |
| `contract_type` | `ContractType` | Categorical | `object` (`str`) | 15 / 15 | 0.0% | 3 | `Month-to-Month` (7), `One Year` (4), `Two Year` (4) |
| `support_tickets` | `SupportTickets` | Discrete Numeric | `int64` | 15 / 15 | 0.0% | 7 | 0 to 6 tickets |
| `payment_method` | `PaymentMethod` | Categorical | `object` (`str`) | 15 / 15 | 0.0% | 4 | `Credit Card` (6), `UPI` (4), `Bank Transfer` (3), `Debit Card` (2) |
| `churned` | `Churn` | Binary Categorical | `object` (`str`) | 15 / 15 | 0.0% | 2 | `Yes` (7), `No` (8) |

---

## 3. Data Cleaning Log & Defensible Assumptions

### Quality Rule Enforcement
1. **Identifier Preservation:** `customer_id` is strictly treated as an atomic nominal identifier and excluded from numerical aggregations.
2. **Column Standardization:** Transformed CamelCase headers to standardized snake_case matching the curriculum specification.
3. **No Silent Row Dropping:** All 15 rows are retained. No data was dropped or arbitrarily altered.
4. **Data Type Casting:** Explicitly cast numerical fields (`age`, `tenure_months`, `support_tickets` to integer; `monthly_charge`, `total_charges` to 2-decimal floats).
5. **Contract Normalization:** Standardized `contract_type` into `contract_type_standard` (`Monthly`, `Annual`, `Biennial`) while retaining raw values.

### Validation Checks & Results
- **Missing Value Audit:** Passed. Exactly 0 nulls across 165 total data points (100% complete).
- **Duplicate Check:** Passed. Exactly 15 unique `customer_id` values (0 duplicates).
- **Impossible Value Check:** Passed:
  - Age: $\min=23, \max=60$ (all valid adult ages $\ge 18$).
  - Tenure: $\min=2, \max=48$ (all $\ge 0$).
  - Monthly Charge: ₹49.99 to ₹149.99 (all $> 0$).
  - Support Tickets: 0 to 6 (all $\ge 0$).
- **Mathematical Consistency Audit:** Passed.
  - Formula verified: $\text{TotalCharges} == \text{MonthlyCharges} \times \text{TenureMonths}$.
  - Result: Discrepancy is ₹0.00 across all 15 records.
- **Outlier Assessment (IQR Method):**
  - Tenure Months: $\text{IQR} = 33.0 - 7.0 = 26.0$. Bounds: $[-32.0, 72.0]$. Maximum value 48 is well within $1.5 \times \text{IQR}$.
  - Support Tickets: $\text{IQR} = 4.0 - 1.0 = 3.0$. Bounds: $[-3.5, 8.5]$. Maximum value 6 is within normal bounds.
  - Monthly Charge: Discrete pricing tiers corresponding exactly to catalog tiers (₹49.99 Basic, ₹79.99 Pro, ₹149.99 Enterprise).

---

## 4. Descriptive Summary Statistics

### Numerical Variables

| Field | Count | Mean | Std Dev | Min | Q1 (25%) | Median | Q3 (75%) | Max | IQR |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `age` | 15 | 39.67 | 11.41 | 23.00 | 30.00 | 38.00 | 47.00 | 60.00 | 17.00 |
| `tenure_months` | 15 | 18.80 | 14.53 | 2.00 | 7.00 | 18.00 | 33.00 | 48.00 | 26.00 |
| `monthly_charge` (₹) | 15 | 84.66 | 43.40 | 49.99 | 49.99 | 79.99 | 114.99 | 149.99 | 65.00 |
| `total_charges` (₹) | 15 | 2,126.54 | 2,423.86 | 99.98 | 449.91 | 1,119.86 | 4,949.67 | 7,199.52 | 4,499.76 |
| `support_tickets` | 15 | 2.53 | 1.88 | 0.00 | 1.00 | 2.00 | 4.00 | 6.00 | 3.00 |

### Categorical Distributions

| Feature | Category | Count | Proportion (%) | Churned Count | Retained Count | Churn Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Contract Type** | `Month-to-Month` | 7 | 46.7% | 7 | 0 | **100.0%** |
| | `One Year` | 4 | 26.7% | 0 | 4 | **0.0%** |
| | `Two Year` | 4 | 26.7% | 0 | 4 | **0.0%** |
| **Subscription Tier** | `Basic` (₹49.99) | 7 | 46.7% | 5 | 2 | **71.4%** |
| | `Pro` (₹79.99) | 4 | 26.7% | 2 | 2 | **50.0%** |
| | `Enterprise` (₹149.99)| 4 | 26.7% | 0 | 4 | **0.0%** |
| **Payment Method** | `UPI` | 4 | 26.7% | 3 | 1 | **75.0%** |
| | `Debit Card` | 2 | 13.3% | 2 | 0 | **100.0%** |
| | `Credit Card` | 6 | 40.0% | 2 | 4 | **33.3%** |
| | `Bank Transfer` | 3 | 20.0% | 0 | 3 | **0.0%** |
| **Gender** | `Female` | 8 | 53.3% | 4 | 4 | **50.0%** |
| | `Male` | 7 | 46.7% | 3 | 4 | **42.9%** |

---

## 5. Comparative Cohort Analysis (Churned vs. Retained)

| Metric | Churned Group ($N=7$) | Retained Group ($N=8$) | Variance / Ratio | Descriptive Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| **Mean Support Tickets** | **4.29 tickets** | **1.00 ticket** | **+329% (4.3x)** | Churned customers experience significantly higher support interaction frequency. |
| **Mean Tenure Months** | **7.00 months** | **29.13 months** | **-76.0%** | Churned customers are overwhelmingly concentrated in early subscription lifecycle. |
| **Mean Age** | **30.71 years** | **47.50 years** | **-35.3%** | Younger customers skew towards short-tenure, month-to-month Basic plans. |
| **Mean Monthly Charge** | **₹67.13** | **₹100.00** | **-32.9%** | Churn is higher in lower-tier plans; Enterprise customers show 0% churn. |
| **Month-to-Month Share** | **100% (7/7)** | **0% (0/8)** | **Absolute split** | Month-to-Month contracts have no friction to cancel when issues arise. |

---

## 6. Actionable Customer Prioritization Matrix

To guide the fictional subscription team, customers are segmented into three operational priority tiers:

1. **Tier 1: Critical Immediate Intervention (Active Month-to-Month with $\ge 3$ tickets, tenure $< 12$m)**
   - *Characteristics:* High friction, short tenure, zero contract lock-in.
   - *Prescribed Action:* Direct telephone contact by Senior Customer Success Manager within 24 hours of 2nd or 3rd ticket. Offer white-glove onboarding and 1-month billing credit or discounted annual upgrade.
2. **Tier 2: Proactive Nurture (Basic / Pro tier with 1–2 tickets, tenure 12–24m)**
   - *Characteristics:* Moderate stability, occasional support friction.
   - *Prescribed Action:* Automated customer satisfaction check-in, product feature education, and annual plan renewal incentive.
3. **Tier 3: Enterprise Relationship Management (Enterprise tier, 2-Year contracts)**
   - *Characteristics:* Zero historical churn, high lifetime value, low ticket volume.
   - *Prescribed Action:* Quarterly business reviews (QBR) and executive sponsorship check-ins.
