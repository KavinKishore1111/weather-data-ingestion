import pandas as pd
from datetime import datetime

def transform(data):
    df = pd.DataFrame(data)
    df["time"] = pd.to_datetime(df["time"])
    df["fetched_at"] = datetime.utcnow()
    return df[["city", "time", "temperature", "windspeed", "winddirection", "weathercode", "fetched_at"]]
    