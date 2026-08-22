import pymysql
import pandas as pd

def fetch_financial_data():
    try:
        # الاتصال بقاعدة البيانات MariaDB المحلّية
        connection = pymysql.connect(
            host='localhost',
            user='dev_user',
            password='password123',
            database='financial_db'
        )
        
        # كتابة استعلام SQL لسحب المعاملات
        query = "SELECT * FROM transactions;"
        
        # قراءة البيانات مباشرة إلى Pandas DataFrame
        df = pd.read_sql(query, connection)
        
        print("✅ Connection successful! Data retrieved from MariaDB:")
        print(df)
        
        # إغلاق الاتصال بقاعدة البيانات
        connection.close()
        return df

    except Exception as e:
        print(f"❌ Error connecting to database: {e}")

if __name__ == "__main__":
    fetch_financial_data()