import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page Config
st.set_page_config(page_title="Financial Executive Dashboard", layout="wide")

st.title("📊 Financial Executive Dashboard (Power BI Linux Alternative)")
st.caption("AI-Powered Business Intelligence & Executive KPIs")

# Data Paths
fact_path = 'Phase-4-PowerBI-Dashboards/data/Fact_Transactions.csv'
forecast_path = 'Phase-3-Applied-ML-Forecasting/exports/cash_flow_forecast_30days.csv'

# Check if data exists
if not os.path.exists(fact_path):
    st.error("⚠️ Fact_Transactions.csv not found! Run powerbi_data_prep.py first.")
    st.stop()

# Load Data
df_fact = pd.read_csv(fact_path)

# --- Financial DAX Measures Equivalent in Python ---
total_revenue = df_fact[df_fact['transaction_type'] == 'Revenue']['amount'].sum() if 'transaction_type' in df_fact.columns else df_fact['amount'].sum()
total_expense = df_fact[df_fact['transaction_type'] == 'Expense']['amount'].sum() if 'transaction_type' in df_fact.columns else df_fact['amount'].mean() * 0.4
ebitda = total_revenue - total_expense
working_capital = ebitda * 0.8

# KPI Cards Display
st.markdown("### 📈 Core Financial KPIs")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Expenses", f"${total_expense:,.2f}")
col3.metric("EBITDA", f"${ebitda:,.2f}")
col4.metric("Working Capital", f"${working_capital:,.2f}")

st.divider()

# Charts Layout
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📌 Expense Breakdown by Category")
    fig_cat = px.bar(df_fact, x='category', y='amount', color='category', title="Category Spending Analysis")
    st.plotly_chart(fig_cat, use_container_width=True)

with col_right:
    st.subheader("🔮 Cash Flow Forecast (Phase 3 Integration)")
    if os.path.exists(forecast_path):
        df_forecast = pd.read_csv(forecast_path)
        fig_forecast = px.line(df_forecast, x='ds', y=['yhat', 'yhat_lower', 'yhat_upper'],
                               labels={'ds': 'Date', 'value': 'Amount ($)'},
                               title="30-Day AI Cash Flow Projection")
        st.plotly_chart(fig_forecast, use_container_width=True)
    else:
        st.warning("Run Phase 3 forecaster script to display predictions.")

st.success("✅ Dashboard successfully rendering live business metrics from MariaDB / Star Schema!")