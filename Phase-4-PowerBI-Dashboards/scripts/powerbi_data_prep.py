import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# ==========================================
# 1. Prepare Star Schema Data for Power BI
# ==========================================

def export_star_schema_for_powerbi():
    print("🗄️ [1/3] Preparing Star Schema tables for Power BI...")
    
    # Engine connection to MariaDB
    try:
        engine = create_engine('mysql+pymysql://dev_user:password123@localhost/financial_db')
        df = pd.read_sql("SELECT * FROM cleaned_financial_records;", con=engine)
    except Exception as e:
        print(f"⚠️ MariaDB connection fallback. Using generated transaction baseline: {e}")
        dates = pd.date_range(start='2025-01-01', periods=100, freq='D')
        df = pd.DataFrame({
            'transaction_date': dates,
            'amount': np.random.uniform(200, 5000, 100),
            'category': np.random.choice(['IT', 'Payroll', 'Marketing', 'Supplies'], 100),
            'transaction_type': np.random.choice(['Expense', 'Revenue'], 100)
        })

    output_dir = 'Phase-4-PowerBI-Dashboards/data'
    os.makedirs(output_dir, exist_ok=True)

    # 1. Fact Table: Fact_Transactions
    fact_transactions = df.copy()
    fact_transactions['date_key'] = pd.to_datetime(fact_transactions['transaction_date']).dt.strftime('%Y%m%d')
    fact_transactions.to_csv(os.path.join(output_dir, 'Fact_Transactions.csv'), index=False)

    # 2. Dimension Table: Dim_Date
    date_range = pd.date_range(start='2024-01-01', end='2026-12-31', freq='D')
    dim_date = pd.DataFrame({
        'date_key': date_range.strftime('%Y%m%d'),
        'FullDate': date_range,
        'Year': date_range.year,
        'Quarter': 'Q' + date_range.quarter.astype(str),
        'Month': date_range.month_name(),
        'MonthNo': date_range.month
    })
    dim_date.to_csv(os.path.join(output_dir, 'Dim_Date.csv'), index=False)

    # 3. Dimension Table: Dim_Category
    categories = df['category'].unique() if 'category' in df.columns else ['General']
    dim_category = pd.DataFrame({'category_id': range(1, len(categories) + 1), 'category_name': categories})
    dim_category.to_csv(os.path.join(output_dir, 'Dim_Category.csv'), index=False)

    print(f"✅ Star Schema files exported successfully to '{output_dir}/'")

# ==========================================
# 2. Python Visual Integration Script for Power BI
# ==========================================

def generate_powerbi_python_visual_script():
    """
    This script template can be pasted directly into Power BI's Python Visual editor.
    """
    python_visual_code = """
# Paste this script inside Power BI Python Visual Editor:
import matplotlib.pyplot as plt
import seaborn as sns

# dataset dataframe is automatically provided by Power BI
plt.figure(figsize=(8,4))
sns.lineplot(data=dataset, x='transaction_date', y='amount', hue='transaction_type', marker='o')
plt.title('AI-Enhanced Cash Flow & Revenue Projection')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
    script_path = 'Phase-4-PowerBI-Dashboards/scripts/powerbi_python_visual.py'
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(python_visual_code)
    print(f"✅ Power BI Python Visual script saved to '{script_path}'")

if __name__ == '__main__':
    export_star_schema_for_powerbi()
    generate_powerbi_python_visual_script()
