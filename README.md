# 🌦️ Real-Time Weather Data Collector

A Python-based ETL pipeline that fetches real-time weather data from [Open-Meteo](https://open-meteo.com/) (no API key required) for multiple cities, transforms the data using Pandas, and stores it into a PostgreSQL database. You can later perform analysis on historical weather patterns such as average temperatures, wind speeds, etc.

---

## ⚙️ Tech Stack

- **Python 3**
- **Pandas** – for data transformation
- **Requests** – for interacting with the API
- **PostgreSQL** – for storing time-series weather data
- **psycopg2-binary** – to connect Python to PostgreSQL

---

## 🔄 Workflow

1. **Extract:**  
   Read city coordinates from a CSV and fetch current weather data using the Open-Meteo API.

2. **Transform:**  
   Normalize the JSON response into a clean Pandas DataFrame with consistent schema.

3. **Load:**  
   Insert the cleaned weather data into a PostgreSQL table (`weather_data`).

4. **Analyze (optional):**  
   Run queries to calculate daily average, min, max temperatures, etc.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

<pre>
git clone https://github.com/your-username/weather_data_collector.git
cd weather_data_collector
</pre>

### 2. Create and Activate Virtual Environment (Optional but Recommended)
<pre>
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
</pre>

### 3. Install Dependencies
<pre>
pip install -r requirements.txt
</pre>

### 4. Set Up PostgreSQL Database
<pre>
-- Run in psql terminal
CREATE USER postgres(username) WITH PASSWORD 'your_password';
CREATE DATABASE weatherdb postgres;
</pre>

### 5. Update config.py with Your DB Credentials
<pre>
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'your_password',
    'dbname': 'weatherdb'
}
</pre>

### 6. Run the Pipeline
<pre>
python main.py
---
Expected output:
🚀 Fetching weather data...
✅ Data loaded successfully.
</pre>


### 7. View Table in PostgreSQL
<pre>
psql -U kavin_postgres -d weatherdb

-- Then in the psql shell:
SELECT * FROM weather_data LIMIT 10;

</pre>

# 🧑‍💻 Author

Kavin Kishore   
B.Tech Student, DTU     
Built as a real-time data engineering mini project.
