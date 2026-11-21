# Customer Churn Dataset - Data Dictionary

| Column Name | Raw Column Name | Data Type | Measurement Type | Unit / Format | Allowed Values / Domain | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `customer_id` | `CustomerID` | String / Text | Nominal Identifier | `CUST-####` | Unique string | No | Synthetic unique identifier for each customer. Never aggregate or compute measures on this field. |
| `gender` | `Gender` | String / Categorical | Nominal | String | `Male`, `Female` | No | Self-reported customer gender. |
| `age` | `Age` | Integer | Ratio | Years | 18 – 100 | No | Customer chronological age in completed years at audit date. Must be >= 18. |
| `tenure_months` | `TenureMonths` | Integer | Ratio | Months | >= 0 | No | Total completed consecutive calendar months since subscription signup. |
| `subscription_type` | `SubscriptionType` | String / Categorical | Ordinal | Text | `Basic`, `Pro`, `Enterprise` | No | Subscription product tier determining feature access and baseline rate. |
| `monthly_charge` | `MonthlyCharges` | Float / Decimal | Ratio | INR (₹) | > 0.00 | No | Fictional recurring monthly billing amount in Indian Rupees (INR). |
| `total_charges` | `TotalCharges` | Float / Decimal | Ratio | INR (₹) | >= 0.00 | No | Cumulative historical charges billed. Reconciles with `monthly_charge * tenure_months`. |
| `contract_type` | `ContractType` | String / Categorical | Nominal | Text | `Month-to-Month`, `One Year`, `Two Year` | No | Raw contractual commitment type. |
| `contract_type_standard` | Derived | String / Categorical | Nominal | Text | `Monthly`, `Annual`, `Biennial` | No | Standardized contract representation normalized for consistency with data guidelines. |
| `support_tickets` | `SupportTickets` | Integer | Discrete Ratio | Count | >= 0 | No | Total customer support inquiries/tickets logged in the preceding 90 days. Key churn proxy. |
| `payment_method` | `PaymentMethod` | String / Categorical | Nominal | Text | `Credit Card`, `Debit Card`, `UPI`, `Bank Transfer` | No | Primary payment instrument on file. |
| `churned` | `Churn` | String / Categorical | Binary | `Yes`, `No` | `Yes`, `No` | No | Target indicator: whether customer cancelled/departed during the observation window. |
| `churn_binary` | Derived | Integer | Binary | 0 or 1 | 0, 1 | No | Quantitative representation of churn status (1 = Yes, 0 = No). |
| `expected_total_charges` | Derived | Float / Decimal | Ratio | INR (₹) | >= 0.00 | No | Audit column: `monthly_charge * tenure_months`. |
| `charge_reconciliation_diff`| Derived | Float / Decimal | Ratio | INR (₹) | 0.00 | No | Audit variance column: `total_charges - expected_total_charges`. Should strictly equal 0.00. |
| `ticket_rate_per_month` | Derived | Float / Decimal | Ratio | Tickets/Month | >= 0.000 | No | Derived support velocity: `support_tickets / tenure_months`. |
| `tenure_band` | Derived | String / Categorical | Ordinal | Text | `0-6m`, `7-12m`, `13-24m`, `25+m` | No | Strategic customer lifecycle cohort. |
| `ticket_tier` | Derived | String / Categorical | Ordinal | Text | `Low (0-1)`, `Moderate (2)`, `Elevated (3-4)`, `Severe (5+)` | No | Customer frustration / risk escalation bracket. |
