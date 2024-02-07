# %% [markdown]
# # Goals:
# 
#     - check what is the top 10 popular characters in the last two decades in the comics, cinema and animation.

# %%
import pandas as pd
import matplotlib.pyplot as plt
import json
from marvel import Marvel
import seaborn as sns
from keys import PUBLIC_KEY, PRIVATE_KEY


# %%
marvel = Marvel(PUBLIC_KEY= PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

# %%
characters = marvel.characters

# %% [markdown]
# # list of avengers heroes

# %%
# Lista dos Vingadores
avengers_heroes = ['Scarlet Witch', 'Wasp', 'Black Widow', 'Hulk', 'Hawkeye', 'Vision', 'Falcon', 'Luke Cage', 'Jessica Jones', 'Black Panther', 'Iron Man', 'Wolverine', 'Storm', 'Iron Patriot', 'Doctor Strange', 'Thor', 'Daredevil', 'Captain America']

# %% [markdown]
# # List of Avengers Villains

# %%
# Lista de codinomes em inglês de alguns vilões dos Vingadores 
avengers_villains = ['Loki', 'Ultron', 'Grandmaster', 'Living Laser', 'Red Skull', 'Super-Adaptoid', 'Crossbones', 'Madame Masque', 'Beyonder', 'Absorbing Man', 'M.O.D.O.K.', 'Lethal Legion', 'Kang', 'Sinister Six', 'Rhino', 'The Hood', 'Grim Reaper', 'Masters of Evil', 'Skrulls', 'Hela', 'Taskmaster', 'Korvac', 'Juggernaut', 'Klaw', 'A.I.M.', 'U-Foes', 'Thanos', 'Blob']

# %% [markdown]
# # List of X-men villains

# %%
# Lista de codinomes em inglês de alguns vilões dos X-Men [avengers_heroes, avengers_villains] , [xmen_villains,]
xmen_villains = [
  'Magneto',
  'The Hand',
  'Pyro',
  'Mystique',
  'Gideon',
  'Lady Deathstrike',
  'Sabretooth',
  'Sebastian Shaw',
  'Shadow King',
  'Apocalypse',
  'Exodus',
  'Onslaught',
  'Emma Frost',
  'Avalanche',
  'Silver Samurai',
  'Cassandra Nova',
  'Mastermind',
  'Master Mold',
  'Dark Phoenix',
  'Juggernaut',
  'William Stryker',
  'Selene',
  'Omega Red',
  'Marauders',
  'Bastion',
  'Loki',
  'Ultron',
  'Grandmaster',
  'Living Laser',
  'Red Skull',
  'Super-Adaptoid',
  'Crossbones',
  'Madame Masque',
  'Beyonder',
  'Absorbing Man',
  'M.O.D.O.K.',
  'Lethal Legion',
  'Kang',
  'Sinister Six',
  'Rhino',
  'The Hood',
  'Grim Reaper',
  'Masters of Evil',
  'Skrulls',
  'Hela',
  'Taskmaster',
  'Korvac',
  'Juggernaut',
  'Klaw',
  'A.I.M.',
  'U-Foes',
  'Thanos',
  'Blob'
  ]

# %% [markdown]
# # List of X-men heroes

# %%
# Lista de codinomes em inglês de alguns heróis dos X-Men 
xmen_heroes = ['Iceman', 'Surge', 'Sunspot', 'Hellion', 'Wolverine', 'Marrow', 'Cannonball', 'Chamber', 'Deadpool', 'Doop', 'Prodigy', 'Strong Guy', 'Jubilee', 'Psylocke', 'Polaris', 'Professor X', 'Hope Summers', 'Storm', 'Emma Frost', 'Forge', 'Multiple Man', 'Bishop', 'Wolfsbane', 'Cypher', 'Warpath', 'Havok', 'Beast', 'Cyclops', 'Cable', 'X-23', 'Longshot', 'Jean Grey', 'Shadowcat', 'Dust', 'Sage', 'Shatterstar', 'Colossus', 'Archangel', 'Anole', 'Fantomex', 'Gambit', 'Rogue', 'Nightcrawler', 'Karma', 'Pixie', 'Elixir', 'Feral', 'Rockslide', 'Domino']

# %% [markdown]
# 

# %% [markdown]
# # List of all Marvel characters

# %%

marvel_all_characters = [
  'Scarlet Witch',
  'Wasp',
  'Black Widow',
  'Hulk',
  'Hawkeye',
  'Vision',
  'Falcon',
  'Luke Cage',
  'Jessica Jones',
  'Black Panther',
  'Iron Man',
  'Wolverine',
  'Storm',
  'Iron Patriot',
  'Doctor Strange',
  'Thor',
  'Daredevil',
  'Captain America',
  'Iceman',
  'Surge',
  'Sunspot',
  'Hellion',
  'Wolverine',
  'Marrow',
  'Cannonball',
  'Chamber',
  'Deadpool',
  'Doop',
  'Prodigy',
  'Strong Guy',
  'Jubilee',
  'Psylocke',
  'Polaris',
  'Professor X',
  'Hope Summers',
  'Storm',
  'Emma Frost',
  'Forge',
  'Multiple Man',
  'Bishop',
  'Wolfsbane',
  'Cypher',
  'Warpath',
  'Havok',
  'Beast',
  'Cyclops',
  'Cable',
  'X-23',
  'Longshot',
  'Jean Grey',
  'Shadowcat',
  'Dust',
  'Sage',
  'Shatterstar',
  'Colossus',
  'Archangel',
  'Anole',
  'Fantomex',
  'Gambit',
  'Rogue',
  'Nightcrawler',
  'Karma',
  'Pixie',
  'Elixir',
  'Feral',
  'Rockslide',
  'Domino',
  'Magneto',
  'The Hand',
  'Pyro',
  'Mystique',
  'Gideon',
  'Lady Deathstrike',
  'Sabretooth',
  'Sebastian Shaw',
  'Shadow King',
  'Apocalypse',
  'Exodus',
  'Onslaught',
  'Emma Frost',
  'Avalanche',
  'Silver Samurai',
  'Cassandra Nova',
  'Mastermind',
  'Master Mold',
  'Dark Phoenix',
  'Juggernaut',
  'William Stryker',
  'Selene',
  'Omega Red',
  'Marauders',
  'Bastion',
  'Loki',
  'Ultron',
  'Grandmaster',
  'Living Laser',
  'Red Skull',
  'Super-Adaptoid',
  'Crossbones',
  'Madame Masque',
  'Beyonder',
  'Absorbing Man',
  'M.O.D.O.K.',
  'Lethal Legion',
  'Kang',
  'Sinister Six',
  'Rhino',
  'The Hood',
  'Grim Reaper',
  'Masters of Evil',
  'Skrulls',
  'Hela',
  'Taskmaster',
  'Korvac',
  'Juggernaut',
  'Klaw',
  'A.I.M.',
  'U-Foes',
  'Thanos',
  'Blob'
  ]

# %%
#lista herois da marvel
marvel_heroes = [
  'Scarlet Witch',
  'Wasp',
  'Black Widow',
  'Hulk',
  'Hawkeye',
  'Vision',
  'Falcon',
  'Luke Cage',
  'Jessica Jones',
  'Black Panther',
  'Iron Man',
  'Wolverine',
  'Storm',
  'Iron Patriot',
  'Doctor Strange',
  'Thor',
  'Daredevil',
  'Captain America',
  'Iceman',
  'Surge',
  'Sunspot',
  'Hellion',
  'Wolverine',
  'Marrow',
  'Cannonball',
  'Chamber',
  'Deadpool',
  'Doop',
  'Prodigy',
  'Strong Guy',
  'Jubilee',
  'Psylocke',
  'Polaris',
  'Professor X',
  'Hope Summers',
  'Storm',
  'Emma Frost',
  'Forge',
  'Multiple Man',
  'Bishop',
  'Wolfsbane',
  'Cypher',
  'Warpath',
  'Havok',
  'Beast',
  'Cyclops',
  'Cable',
  'X-23',
  'Longshot',
  'Jean Grey',
  'Shadowcat',
  'Dust',
  'Sage',
  'Shatterstar',
  'Colossus',
  'Archangel',
  'Anole',
  'Fantomex',
  'Gambit',
  'Rogue',
  'Nightcrawler',
  'Karma',
  'Pixie',
  'Elixir',
  'Feral',
  'Rockslide',
  'Domino'
  ] 

# %%
# lista de viloes
marvel_villains = [
  'Scarlet Witch',
  'Wasp',
  'Black Widow',
  'Hulk',
  'Hawkeye',
  'Vision',
  'Falcon',
  'Luke Cage',
  'Jessica Jones',
  'Black Panther',
  'Iron Man',
  'Wolverine',
  'Storm',
  'Iron Patriot',
  'Doctor Strange',
  'Thor',
  'Daredevil',
  'Captain America',
  'Iceman',
  'Surge',
  'Sunspot',
  'Hellion',
  'Wolverine',
  'Marrow',
  'Cannonball',
  'Chamber',
  'Deadpool',
  'Doop',
  'Prodigy',
  'Strong Guy',
  'Jubilee',
  'Psylocke',
  'Polaris',
  'Professor X',
  'Hope Summers',
  'Storm',
  'Emma Frost',
  'Forge',
  'Multiple Man',
  'Bishop',
  'Wolfsbane',
  'Cypher',
  'Warpath',
  'Havok',
  'Beast',
  'Cyclops',
  'Cable',
  'X-23',
  'Longshot',
  'Jean Grey',
  'Shadowcat',
  'Dust',
  'Sage',
  'Shatterstar',
  'Colossus',
  'Archangel',
  'Anole',
  'Fantomex',
  'Gambit',
  'Rogue',
  'Nightcrawler',
  'Karma',
  'Pixie',
  'Elixir',
  'Feral',
  'Rockslide',
  'Domino'
  ]

# %%
# criando dataframe 
chacter_df = pd.DataFrame(columns=['ID', 'Name', 'Comics', 'Series', 'Events', 'Stories'])
chacter_df

# %% [markdown]
# # Function to get charactere names for a list and look for their names in the API returning a dataframe.

# %%
# funcao para receber personagens
def get_character(ave):
    list_char = []
    character_df = pd.DataFrame(columns=['ID', 'Name', 'Comics', 'Series', 'Events', 'Stories'])
    characters = marvel.characters
    for c in ave:
        avengers = characters.all(name=c)['data']['results']
        for char in avengers:
            char_ = {'ID': char['id'], 'Name': char['name'], 'Comics': char['comics']['available']}
            char_['Series'] = char['series']['available']
            char_['Events'] = char['events']['available']
            char_['Stories'] = char['stories']['available']
            list_char.append(char_)
    character_df = pd.DataFrame(list_char)
    return character_df


# %%
marvel_all_characters_df = get_character(marvel_all_characters)
marvel_all_characters_df["Name"]

# %%
marvel_all_characters_df

# %% [markdown]
# # Taking the list os characters to check is any of them are duplicated 

# %%
def check_valid_names(list_,df_):
    valores_comuns = list(set(list_).intersection(set(df_)))
    return valores_comuns

# %%
checked_avengers = check_valid_names(avengers_heroes, avengers_all_characters_df['Name'])
print(checked_avengers)
print(len(checked_avengers))

# %%
def joing_teams(h, v):
    new_c = []
    new_c.append(v)
    new_c.append(h)
    return new_c    
#[avengers_heroes, avengers_villains], [xmen_villains, xmen_heroes], [marvel_villains, marvel_heroes]

# %%
villains_team = joing_teams(avengers_villains, xmen_villains)

# %%
heroes_team = joing_teams(xmen_heroes, avengers_heroes)

# %%
marvel_char = joing_teams(marvel_villains, marvel_heroes)

# %% [markdown]
# # Taking the list and turning in a dic and separate them by hero and villain 

# %%
def add_class_hero(x):
    char_ = {'Avengers':[], 'X-Men':[],'X-Men-Avengers':[] }
    char_['Avengers'] = x[0]
    char_['X-Men'] = x[1]
    char_['X-Men-Avengers'] = list(set(x[0]).intersection(set(x[1])))
    return char_



# %%
def add_class_villain(x):
    char_ = {'Villain_Avengers':[], 'Villain_X-Men':[]}
    char_['Villain_X-Men'] = x[0]
    char_['Villain_Avengers'] = x[1] 
    return char_

# %%
class_hero = add_class_hero(heroes_team)


# %%
class_villains = add_class_villain(villains_team)


# %%
class_marvel = class_villains.copy()
class_marvel.update(class_hero)
class_marvel 

# %%
def transfer_class_df(x):
    for key, value in class_marvel.items():
        if x in value:
            return key

# %%
marvel_all_characters_df["Class"] = marvel_all_characters_df["Name"].apply(transfer_class_df)
marvel_all_characters_df

# %% [markdown]
# # Visualization
#     - Check data types
#     - Check data size
#     - Do tables

# %% [markdown]
# # Check data types

# %%
marvel_all_characters_df.info()

# %%
### Describing a numeric Series
marvel_all_characters_df.describe()

# %% [markdown]
# # Check data size

# %%
marvel_all_characters_df.count()

# %% [markdown]
# # Tables

# %% [markdown]
# # Top 5 Avengers with more comics 

# %%
# condicial para filtras por classe
conditiona_1 = marvel_all_characters_df[marvel_all_characters_df['Class'] == 'Avengers']

# %%
# Top 8 with more comics Conditional_1 = 
top_comics_avengers_names = conditiona_1.nlargest(8, 'Comics')[['Name', 'Comics']].drop_duplicates()

# Result
print(type(top_comics_names))
top_comics_names


# %% [markdown]
# # Groupby with conditional  

# %%
class_avengers_by_comics = (
    conditiona_1.nlargest(8, 'Comics')[['Name', 'Comics']].groupby(['Name', 'Comics'])
    .size()
    .reset_index(name='Count')
    .sort_values('Comics', ascending=True)
    .drop_duplicates('Name')
    
)
class_by_comics

# %% [markdown]
# # Function to filter a Conditioal by reference column, principal column

# %%
# funcao que filtra coluna por valor, Exemplo: 
    # conditional = marvel_all_characters_df[marvel_all_characters_df['Class'] == 'Villain_Avengers']
def sort_one_columns(df, column, column_value):
    sort = df[df[column] == column_value].drop_duplicates()
    return sort

# %%
# funcao que filtra uma coluna por diferentes valores, Exemplo: 
    # conditional = marvel_all_characters_df[(marvel_all_characters_df['Class'] == 'Avengers') | (marvel_all_characters_df['Class'] == 'Villain_Avengers')]
def sort_two_columns(df, column, column_one_value, column_two_value):
    sort = df[(df[column] == column_one_value) | (df[column] == column_two_value)].drop_duplicates()
    return sort

# %%
# funcao para aplicar uma condicional pegando os 5 maiores valores de uma coluna Exemplo: 
    # top_comics_avengers_villain_names = conditional.nlargest(5, 'Comics')[['Name', 'Comics']
def add_conditial(variable, principal_column, reference_column):
    cond = variable.nlargest(10, principal_column)[[reference_column, principal_column]].drop_duplicates()
    return cond


# %%
def Filter_comic_class(conditional, reference_column, principal_column):
    filter_ = (
    conditional.groupby([reference_column, principal_column])
    .size()
    .reset_index(name='Count')
    .sort_values(principal_column, ascending=True)
    .drop_duplicates(reference_column)
    )
    return filter_
    

# %%
def visual_plot(variable, x_column, y_column, x_lable, y_lable, title ):
    sns.barplot(x=x_column, y=y_column, data=variable, palette="Blues")
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.show()

# %%
conditional_5 = sort_two_columns(marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')
conditional_5

# %%
top_comics_avengers_world = add_conditial(conditional_5, 'Comics', 'Name')
top_comics_avengers_world

# %%
top_8_avengers_world = Filter_comic_class(top_comics_avengers_world, 'Name', 'Comics')
top_8_avengers_world

# %%
visual_plot(top_8_avengers_world, "Name", "Comics", "Name", "Number of Comics", "The Top 10 in Avenger's world with more comics" )

# %%
conditional_10 = sort_two_columns(marvel_all_characters_df, 'Class', 'X-Men', 'Villain_X-Men')
conditional_10

# %%
top_comics_xmen_world = add_conditial(conditional_10, 'Comics', 'Name')
top_comics_xmen_world

# %%
top_10_xmen_world = Filter_comic_class(top_comics_xmen_world, 'Name', 'Comics')
top_10_xmen_world

# %%
visual_plot(top_10_xmen_world, "Name", "Comics", "Name", "Number of Comics", "The Top 10 in X-men's world with more comics" )

# %%
def add_conditial_20(variable, principal_column, reference_column):
    cond = variable.nlargest(20, principal_column)[[reference_column, principal_column]].drop_duplicates()
    return cond

# %%
top_comics_marvel_world = add_conditial_20(marvel_all_characters_df, 'Comics', 'Name')
top_comics_marvel_world

# %%
top_marvels_world = Filter_comic_class(top_comics_marvel_world, 'Name', 'Comics')
top_marvels_world

# %%
visual_plot(top_marvels_world, "Name", "Comics", "Name", "Number of Comics", "The Top 20 in Marvel's world with more comics" )

# %%
def sort_two_columns_(df, column, column_one_value, column_two_value):
    sort = df[(df[column] == column_one_value) | (df[column] == column_two_value)].drop_duplicates()
    return sort

# %%
# Calcular a porcentagem de Vingadores em relação ao total
total_avengers_comics_ = sort_two_columns_(marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')
total_xmen_comics_ = sort_two_columns_(marvel_all_characters_df, 'Class', 'X-Men', 'Villain_X-Men')
total_xmen_comics_


# %%

percentage_avengers = (total_avengers_comics_['Comics'].sum() / (total_avengers_comics_['Comics'].sum() + total_xmen_comics_['Comics'].sum())) * 100

print(f"A porcentagem de comics dos Vingadores em relação ao total é: {percentage_avengers:.2f}%")
percentage_avengers

# %%
result_df = pd.DataFrame({'Equipe': ['Vingadores'], 'Porcentagem': [percentage_avengers]})
result_df

# %%

percentage_avengers = (total_avengers_comics_['Comics'].sum() / (total_avengers_comics_['Comics'].sum() + total_xmen_comics_['Comics'].sum())) * 100
percentage_xmen = 100 - percentage_avengers  # Porcentagem dos X-Men


# Criar DataFrame com os resultados
result_df = pd.DataFrame({'Class': ['Avengers', 'X-Men'], 'Percentage': [percentage_avengers, percentage_xmen]})
print(result_df)



# %%
visual_plot(result_df, "Class", "Percentage", "Class", "Percentage", 'Percentage of Avengers and X-Men Comics in Relation to the Total')

# %%
perc = result_df['Percentage']
perc
lab = result_df['Class']

# %%
perc.plot.pie(autopct="%.1f%%",labels=lab, textprops={'fontsize':14}, colors=sns.color_palette('Blues'))




# %%
