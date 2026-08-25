import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

url = os.getenv("DATABASE_URL")
url1 = os.getenv("DATABASE_URL1")

engine = create_engine(url)
engine1 = create_engine(url1)

tables = [
    "stop_times",
    "trips",
    "stops",
    "routes",
    "agency",
    "calendar",
    "calendar_dates",
    "transfers",
]

for table_name in tables:
    df = pd.read_sql_table(table_name, engine)
    df.to_sql(table_name, engine1, if_exists="replace", index=False)
    print(f"Migration de la table {table_name} terminée !")
