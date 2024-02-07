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
characters = marvel.characters


# Calling the function to extract the data
marvel_all_characters_df = ext.get_character(ext.marvel_all_characters)





# Visualization

# Calling the data to create the graphics 
viz.visual_plot(viz.top_avengers, "Name", "Comics", "Name", "Number of Comics", 'The Top 8 Avengers with more comics')

viz.visual_plot(viz.top_villain, "Name", "Comics", "Name", "Number of Comics", 'The Top 8 Avengers Villains with more comics')

viz.visual_plot(viz.top_8_avengers_world, "Name", "Comics", "Name", "Number of Comics", "The Top 8 in Avenger's world with more comics" )



# 2. Transforming
tr.build_dataframe (marvel_all_characters_df)
