import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from prophet import Prophet
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, mean_absolute_error, mean_squared_error

# ==========================================
# 1. Fetch & Prepare Historical Data
# ==========================================

def fetch_prepared_data():
    print("🗄️ [1/4] Fetching historical records from MariaDB...")
    try:
        engine = create_engine('mysql+pymysql://dev_user:password123@localhost/financial_db')
        df = pd.read_sql("SELECT * FROM cleaned_financial_records;", con=engine)
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        print(f"✅ Loaded {len(df)} transactions.")
        return df
    except Exception as e:
        print(f"⚠️ Database fallback: Generating synthetic dataset due to: {e}")
        # Synthetic data fallback for testing ML model pipelines
        dates = pd.date_range(start='2025-01-01', periods=180, freq='D')
        amounts = np.random.normal(loc=1500, scale=300, size=180)
        categories = np.random.choice(['groceries', 'payroll', 'marketing', 'it'], size=180)
        df = pd.DataFrame({'transaction_date': dates, 'amount': amounts, 'category': categories})
        return df

# ==========================================
# 2. Time Series Forecasting (Prophet Model)
# ==========================================

def forecast_cash_flow(df):
    print("\n📈 [2/4] Training Prophet model for Cash Flow Forecasting...")
    
    # Prophet requires specific column names: 'ds' for dates and 'y' for values
    daily_df = df.groupby('transaction_date')['amount'].sum().reset_index()
    daily_df.columns = ['ds', 'y']
    
    # Initialize & Fit Prophet Model (yearly_seasonality set to False for short histories)
    model = Prophet(yearly_seasonality=False, daily_seasonality=False)
    model.fit(daily_df)
    
    # Create Future Dates DataFrame for Next 30 Days
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    # Evaluate MAE & RMSE on historical baseline
    y_true = daily_df['y'].values
    y_pred = forecast['yhat'][:len(daily_df)].values
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    
    print(f"✅ Forecast Completed! Model Error Metrics -> MAE: ${mae:.2f} | RMSE: ${rmse:.2f}")
    
    # Return 30-day forecast projection
    forecast_results = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30)
    return forecast_results

# ==========================================
# 3. Credit Risk & Default Prediction (Random Forest)
# ==========================================

def train_credit_risk_model():
    print("\n🌲 [3/4] Training Random Forest Classifier for Risk Assessment...")
    
    # Simulating features: transaction_amount, payment_delay_days, credit_score_ratio
    np.random.seed(42)
    n_samples = 500
    X = pd.DataFrame({
        'transaction_amount': np.random.uniform(50, 10000, n_samples),
        'payment_delay_days': np.random.randint(0, 60, n_samples),
        'credit_score_ratio': np.random.uniform(0.3, 0.95, n_samples)
    })
    # Target: 1 if high risk/default, 0 if safe
    y = np.where((X['payment_delay_days'] > 30) | (X['credit_score_ratio'] < 0.5), 1, 0)
    
    # Train/Test Split (Fixed parameter name: test_size)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest Classifier
    rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_clf.fit(X_train, y_train)
    
    # Predictions & Accuracy Evaluation
    predictions = rf_clf.predict(X_test)
    print("✅ Classifier Evaluation Metrics:")
    print(classification_report(y_test, predictions, target_names=['Low Risk', 'High Risk']))
    
    return rf_clf

# ==========================================
# 4. Pipeline Execution & Export
# ==========================================

def run_ml_pipeline():
    # Ensure export output directory exists
    output_dir = 'Phase-3-Applied-ML-Forecasting/exports'
    os.makedirs(output_dir, exist_ok=True)
    
    # Execute Pipeline
    raw_data = fetch_prepared_data()
    forecast_df = forecast_cash_flow(raw_data)
    risk_model = train_credit_risk_model()
    
    # Save Predictions to CSV
    export_path = os.path.join(output_dir, 'cash_flow_forecast_30days.csv')
    forecast_df.to_csv(export_path, index=False)
    print(f"\n🎉 ML Pipeline completed successfully! Forecast saved to: {export_path}")

if __name__ == '__main__':
    run_ml_pipeline()