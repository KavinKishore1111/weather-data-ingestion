import psycopg2
from config import DB_CONFIG
from etl.sql_queries import CREATE_TABLE_QUERY, INSERT_WEATHER_QUERY

def load_to_postgresql(df):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(CREATE_TABLE_QUERY)

        for _, row in df.iterrows():
            cursor.execute(INSERT_WEATHER_QUERY, tuple(row))

        conn.commit()
        print("✅ Data loaded successfully.")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        cursor.close()
        conn.close()
