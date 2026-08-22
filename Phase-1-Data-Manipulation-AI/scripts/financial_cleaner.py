cat << 'EOF' > Phase-1-Data-Manipulation-AI/scripts/financial_cleaner.py
import pandas as pd
import numpy as np
import os

def clean_financial_data(input_file, output_file):
    print("🚀 Starting Financial Data Cleaning Process...")
    
    # 1. Load Raw Data
    if not os.path.exists(input_file):
        print(f"❌ Error: File {input_file} not found.")
        return
        
    df = pd.read_csv(input_file)
    print(f"📊 Loaded {len(df)} raw transaction records.")

    # 2. Remove Duplicates
    df = df.drop_duplicates()

    # 3. Clean Currency and Amount Column
    df['Amount_Clean'] = df['Amount'].astype(str).str.replace('$', '', regex=False)
    df['Amount_Clean'] = df['Amount_Clean'].str.replace('+', '', regex=False)
    df['Amount_Clean'] = df['Amount_Clean'].astype(float)

    # 4. Format Dates
    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

    # 5. Handle Missing Categories (Rule-based / Fallback)
    df['Department'] = df['Department'].fillna('Unassigned/Pending_AI')

    # 6. Calculate Financial KPIs
    total_revenue = df[df['Amount_Clean'] > 0]['Amount_Clean'].sum()
    total_expenses = abs(df[df['Amount_Clean'] < 0]['Amount_Clean'].sum())
    net_cash_flow = total_revenue - total_expenses

    print("\n--- 📈 Financial Summary ---")
    print(f"Total Revenue:  ${total_revenue:,.2f}")
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Net Cash Flow:  ${net_cash_flow:,.2f}")
    print("----------------------------\n")

    # 7. Save Cleaned Dataset
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data successfully saved to: {output_file}")

if __name__ == "__main__":
    input_path = "Phase-1-Data-Manipulation-AI/data/raw_financial_data.csv"
    output_path = "Phase-1-Data-Manipulation-AI/data/cleaned_financial_data.csv"
    clean_financial_data(input_path, output_path)
EOF