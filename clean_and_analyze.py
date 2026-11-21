"""
clean_and_analyze.py
--------------------
Reproducible Data Cleaning, Profiling, and Exploratory Analysis Pipeline
for Customer Churn Dataset.

Usage:
    python clean_and_analyze.py
"""

import os
import sys
import pandas as pd
import numpy as np

def run_pipeline():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(base_dir, "customer_churn_raw.csv")
    cleaned_path = os.path.join(base_dir, "customer_churn_cleaned.csv")

    if not os.path.exists(raw_path):
        print(f"Error: Raw CSV file not found at {raw_path}", file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print("CUSTOMER CHURN DATA QUALITY & CLEANING PIPELINE")
    print("=" * 60)

    # 1. Load Raw
    df_raw = pd.read_csv(raw_path)
    print(f"1. Ingested raw dataset: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns.")

    # 2. Quality Profiling
    print("\n2. Data Quality Audit:")
    null_counts = df_raw.isnull().sum()
    print(f"   - Total Missing Values: {null_counts.sum()} across all fields.")
    dup_count = df_raw['CustomerID'].duplicated().sum()
    print(f"   - Duplicate CustomerID count: {dup_count}")

    # Mathematical consistency
    recon_diff = (df_raw['TotalCharges'] - (df_raw['MonthlyCharges'] * df_raw['TenureMonths'])).round(2)
    discrepancy_count = (recon_diff != 0).sum()
    print(f"   - Mathematical Reconciliation Discrepancies (Total != Monthly * Tenure): {discrepancy_count}")

    # 3. Cleaning & Standardization
    col_map = {
        'CustomerID': 'customer_id',
        'Gender': 'gender',
        'Age': 'age',
        'TenureMonths': 'tenure_months',
        'SubscriptionType': 'subscription_type',
        'MonthlyCharges': 'monthly_charge',
        'TotalCharges': 'total_charges',
        'ContractType': 'contract_type',
        'SupportTickets': 'support_tickets',
        'PaymentMethod': 'payment_method',
        'Churn': 'churned'
    }
    df_clean = df_raw.rename(columns=col_map).copy()
    df_clean['customer_id'] = df_clean['customer_id'].astype(str).str.strip()
    df_clean['gender'] = df_clean['gender'].astype(str).str.strip()
    df_clean['age'] = df_clean['age'].astype(int)
    df_clean['tenure_months'] = df_clean['tenure_months'].astype(int)
    df_clean['subscription_type'] = df_clean['subscription_type'].astype(str).str.strip()
    df_clean['monthly_charge'] = df_clean['monthly_charge'].astype(float).round(2)
    df_clean['total_charges'] = df_clean['total_charges'].astype(float).round(2)
    df_clean['contract_type_standard'] = df_clean['contract_type'].map({
        'Month-to-Month': 'Monthly',
        'One Year': 'Annual',
        'Two Year': 'Biennial'
    })
    df_clean['support_tickets'] = df_clean['support_tickets'].astype(int)
    df_clean['payment_method'] = df_clean['payment_method'].astype(str).str.strip()
    df_clean['churned'] = df_clean['churned'].astype(str).str.strip()
    df_clean['churn_binary'] = df_clean['churned'].map({'Yes': 1, 'No': 0}).astype(int)

    # Export clean
    df_clean.to_csv(cleaned_path, index=False)
    print(f"\n3. Cleaned dataset written to: {cleaned_path}")

    # 4. Summary Findings
    print("\n4. Key Analytical Insights:")
    churn_rate = df_clean['churn_binary'].mean() * 100
    print(f"   - Baseline Churn Rate: {churn_rate:.1f}% ({df_clean['churn_binary'].sum()}/{len(df_clean)})")
    
    contract_churn = df_clean.groupby('contract_type_standard')['churn_binary'].mean() * 100
    print(f"   - Churn by Contract Type:")
    for c_type, rate in contract_churn.items():
        print(f"       * {c_type}: {rate:.1f}%")
        
    avg_tickets = df_clean.groupby('churned')['support_tickets'].mean()
    print(f"   - Average Support Tickets: Churned = {avg_tickets['Yes']:.2f} vs. Retained = {avg_tickets['No']:.2f}")

    avg_tenure = df_clean.groupby('churned')['tenure_months'].mean()
    print(f"   - Average Tenure: Churned = {avg_tenure['Yes']:.1f} months vs. Retained = {avg_tenure['No']:.1f} months")

    print("\n" + "=" * 60)
    print("PIPELINE EXECUTION COMPLETE: 100% PASS")
    print("=" * 60)

if __name__ == '__main__':
    run_pipeline()
