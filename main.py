import pandas as pd
import matplotlib.pyplot as plt
from marvel import Marvel
import seaborn as sns
from keys import PUBLIC_KEY, PRIVATE_KEY

import src.extracting as ext
import src.transforming as tr
import src.visualization as viz





# 1. Extracting
marvel = Marvel(PUBLIC_KEY= PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)
#characters = marvel.characters

# Calling the function to extract the data
marvel_all_characters_df = ext.get_character(ext.marvel_all_characters, marvel)

# Joing all the lists
villains_team = ext.joing_teams(ext.avengers_villains, ext.xmen_villains)
heroes_team = ext.joing_teams(ext.xmen_heroes, ext.avengers_heroes)

# Calling the function add_class
class_hero = ext.add_class_hero(heroes_team)
class_villains =ext. add_class_villain(villains_team)

# Class Marvel
class_marvel = class_villains.copy()
class_marvel.update(class_hero)

# DF receive the attribute value in a new column by the name
marvel_all_characters_df["Class"] = marvel_all_characters_df["Name"].apply(ext.transfer_class_df)
marvel_all_characters_df



# 2. Transforming
df = tr.build_dataframe (marvel_all_characters_df)

# 3. Visualizing
viz.barplot_price(df)
viz.barplot_count(df)

# 4. Voice feedback
os.system("say report created")