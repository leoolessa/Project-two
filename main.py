import pandas as pd
import matplotlib.pyplot as plt
from marvel import Marvel
import seaborn as sns


import src.extracting as ext
import src.transforming as tr
import src.visualization as viz





# 1. Extracting
marvel_all_characters_df = ext.get_character(ext.marvel_all_characters)


# 2. Transforming
df = tr.build_dataframe (ext.marvel_all_characters_df)

# 3. Visualizing
viz.barplot_price(df)
viz.barplot_count(df)

# 4. Voice feedback
os.system("say report created")