import pandas as pd
import sqlite3
df = pd.read_csv("data/processed/all_funds_cleaned.csv")
conn = sqlite3.connect("mutual_funds.db")
df.to_sql("nav_history", conn, if_exists="replace", index=False)
print("database created successfully!")
conn.close()