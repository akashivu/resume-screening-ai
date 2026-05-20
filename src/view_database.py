import sqlite3
import pandas as pd

connection = sqlite3.connect(
    "resume_screening.db"
)

query = "SELECT * FROM resume_analysis"

df = pd.read_sql(query, connection)

print(df)