import psycopg2
import pandas as pd
from config import DB_CONFIG

def daily_avg():
    conn = psycopg2.connect(**DB_CONFIG)
    query = """
        SELECT city, DATE(time) as date, 
               AVG(temperature) as avg_temp, 
               MIN(temperature) as min_temp,
               MAX(temperature) as max_temp
        FROM weather_data
        GROUP BY city, DATE(time)
        ORDER BY date DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, conn)
    print(df)
    conn.close()

if __name__ == "__main__":
    daily_avg()
