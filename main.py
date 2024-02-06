import pandas as pd
import matplotlib.pyplot as plt
from marvel import Marvel
import seaborn as sns


import src.extracting as ext
import src.transforming as tr
import src.visualization as viz





# 1. Extracting

# Calling the function to extract the data
marvel_all_characters_df = ext.get_character(ext.marvel_all_characters)

# Joing all the lists
villains_team = ext.joing_teams(ext.avengers_villains, ext.xmen_villains)
heroes_team = ext.joing_teams(ext.xmen_heroes, ext.avengers_heroes)

# Calling the function add_class
class_hero = ext.add_class_hero(heroes_team)
class_villains = ext.add_class_villain(villains_team)

# Class Marvel
class_marvel = class_villains.copy()
class_marvel.update(class_hero)

# DF receive the attribute value in a new column by the name
marvel_all_characters_df["Class"] = marvel_all_characters_df["Name"].apply(ext.transfer_class_df)


# Visualization

# Calling the sort functions
avengers_hero_sort = viz.sort_one_column(marvel_all_characters_df,'Class', 'Avengers')

avengers_villain_sort = viz.sort_one_column(marvel_all_characters_df,'Class', 'Villain_Avengers')

avengers_and_villain_sort = viz.sort_two_columns(marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')

# Calling the conditional function
top_avengers = viz.add_conditial(avengers_hero_sort, 'Comics', 'Name')

top_villain = viz.add_conditial(avengers_villain_sort, 'Comics', 'Name')

top_comics_avengers_world = viz.add_conditial(avengers_and_villain_sort, 'Comics', 'Name')

# Calling the Filter function
top_8_avengers = viz.Filter_comic_class(top_avengers, 'Name', 'Comics')

top_8_villain = viz.Filter_comic_class(top_villain, 'Name', 'Comics')

top_8_avengers_world = viz.Filter_comic_class(top_comics_avengers_world, 'Name', 'Comics')


# Visualization
viz.visual_plot(top_avengers, "Name", "Comics", "Name", "Number of Comics", 'The Top 8 Avengers with more comics')

viz.visual_plot(top_villain, "Name", "Comics", "Name", "Number of Comics", 'The Top 8 Avengers Villains with more comics')

viz.visual_plot(top_8_avengers_world, "Name", "Comics", "Name", "Number of Comics", "The Top 8 in Avenger's world with more comics" )







# 2. Transforming
df = tr.build_dataframe (marvel_all_characters_df)

# 3. Visualizing
viz.barplot_price(df)
viz.barplot_count(df)

# 4. Voice feedback
os.system("say report created")