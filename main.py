# main.py
from etl.extract import fetch_weather
from etl.transform import transform
from etl.load import load_to_postgresql

def main():
    print("🚀 Fetching weather data...")
    raw = fetch_weather()
    df = transform(raw)
    load_to_postgresql(df)

if __name__ == "__main__":
    main()
