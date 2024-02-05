import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import os
import matplotlib.pyplot as plt

from src.extracting import get_description_from_link
 

def build_dataframe (df):
    # 0. Get time
    ts = int(time.time())
    
    # 3. Export
    name = f"marvel-{ts}.csv"
    df.to_csv(f"data/{name}", index=False)
    
    return df