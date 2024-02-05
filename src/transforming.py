import pandas as pd
import time


def build_dataframe (df):
    # 0. Get time
    ts = int(time.time())
    
    # 3. Export
    name = f"marvel-{ts}.csv"
    df.to_csv(f"data/{name}", index=False)
    
    return df