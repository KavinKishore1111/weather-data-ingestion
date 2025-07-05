CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS weather_data (
    city TEXT,
    time TIMESTAMP,
    temperature REAL,
    windspeed REAL,
    winddirection REAL,
    weathercode INT,
    fetched_at TIMESTAMP
);
"""

INSERT_WEATHER_QUERY = """
INSERT INTO weather_data 
(city, time, temperature, windspeed, winddirection, weathercode, fetched_at)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
