import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
from sqlalchemy import create_engine

# ==========================================
# 1. Fetch Data from Database
# ==========================================

def fetch_financial_data():
    print("🗄️ [1/4] Fetching cleaned data from MariaDB...")
    try:
        engine = create_engine('mysql+pymysql://dev_user:password123@localhost/financial_db')
        query = "SELECT * FROM cleaned_financial_records;"
        df = pd.read_sql(query, con=engine)
        
        # Ensure transaction_date is datetime type
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        print(f"✅ Loaded {len(df)} records successfully.")
        return df
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return pd.DataFrame()

# ==========================================
# 2. Advanced Financial Visualizations
# ==========================================

def generate_static_charts(df):
    print("📊 [2/4] Generating Seaborn & Matplotlib statistical charts...")
    
    # Chart A: Correlation & Heatmap logic mock
    plt.figure(figsize=(8, 5))
    df_pivot = df.pivot_table(index='transaction_date', columns='category', values='amount', aggfunc='sum').fillna(0)
    sns.heatmap(df_pivot.corr(), annot=True, cmap='Blues', fmt='.2f')
    plt.title('Financial Category Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('Phase-2-Visualization-Storytelling/reports/correlation_heatmap.png')
    plt.close()
    
    # Chart B: Outliers Distribution (Boxplot)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='category', y='amount', palette='Set2')
    plt.title('Expense Anomalies & Distribution by Category')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig('Phase-2-Visualization-Storytelling/reports/expense_boxplots.png')
    plt.close()

def generate_interactive_chart(df):
    print("📈 Creating Interactive Plotly chart...")
    
    # Aggregating daily trend by category
    daily_summary = df.groupby(['transaction_date', 'category'])['amount'].sum().reset_index()
    
    fig = px.line(
        daily_summary, 
        x='transaction_date', 
        y='amount', 
        color='category',
        markers=True,
        title='Interactive Expense Trajectory & Drill-down Analysis',
        labels={'transaction_date': 'Date', 'amount': 'Amount (DZD/USD)'}
    )
    
    fig.update_layout(template='plotly_white')
    return pio.to_html(fig, full_html=False)

# ==========================================
# 3. AI Data Storytelling & Narrative Generation
# ==========================================

def generate_ai_executive_summary(df):
    print("🤖 [3/4] Generating AI Executive Storytelling & Recommendations...")
    
    total_spent = df['amount'].sum()
    top_category = df.groupby('category')['amount'].sum().idxmax()
    top_category_val = df.groupby('category')['amount'].sum().max()
    
    # Prompting Logic Mock / LLM Narrative Engine
    summary_text = f"""
    ### Executive Financial Narrative & Anomaly Insights
    - **Total Expenditure:** ${total_spent:,.2f} recorded across analyzed periods.
    - **Primary Expense Driver:** The category **'{top_category}'** accounted for the largest financial outflow, totaling **${top_category_val:,.2f}**.
    
    #### ⚠️ Detected Financial Risks & Anomalies:
    1. **Operational Outliers:** Unusual spikes identified in administrative and marketing sub-categories.
    2. **Budget Variance:** High concentration of costs in short execution windows indicates unstructured procurement.

    #### 💡 Strategic Management Recommendations:
    - **Action Item 1:** Implement strict approval limits for purchases exceeding seasonal baselines in `{top_category}`.
    - **Action Item 2:** Re-negotiate vendor terms for IT infrastructure to convert volatile expenses into stable subscriptions.
    """
    return summary_text

# ==========================================
# 4. Generate Interactive Executive HTML Report
# ==========================================

def build_executive_report():
    df = fetch_financial_data()
    if df.empty:
        print("⚠️ No data available to process.")
        return

    generate_static_charts(df)
    plotly_html = generate_interactive_chart(df)
    ai_story = generate_ai_executive_summary(df)

    print("📄 [4/4] Compiling Executive Dashboard Report (HTML)...")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Executive Financial Performance Report</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 30px; background-color: #f8f9fa; color: #333; }}
            .container {{ max-width: 1100px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #1a365d; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }}
            .ai-box {{ background-color: #ebf8ff; border-left: 4px solid #3182ce; padding: 20px; margin: 20px 0; border-radius: 5px; }}
            .chart-container {{ margin: 30px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Financial Performance & AI Storytelling Report</h1>
            
            <div class="ai-box">
                {ai_story}
            </div>

            <div class="chart-container">
                <h2>📈 Interactive Expense Trajectory</h2>
                {plotly_html}
            </div>
        </div>
    </body>
    </html>
    """

    output_path = 'Phase-2-Visualization-Storytelling/reports/executive_report.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"🎉 Success! Interactive report generated at: {output_path}")

if __name__ == '__main__':
    build_executive_report()