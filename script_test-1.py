
# %%
import pandas as pd
import matplotlib.pyplot as plt
from marvel import Marvel
import seaborn as sns
import time
from keys import PUBLIC_KEY, PRIVATE_KEY



marvel = Marvel(PUBLIC_KEY= PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)
characters = marvel.characters



# Lista dos Vingadores
avengers_heroes = ['Scarlet Witch', 'Wasp', 'Black Widow', 'Hulk', 'Hawkeye', 'Vision', 'Falcon', 'Luke Cage', 'Jessica Jones', 'Black Panther', 'Iron Man', 'Wolverine', 'Storm', 'Iron Patriot', 'Doctor Strange', 'Thor', 'Daredevil', 'Captain America']


# # List of Avengers Villains


# Lista de codinomes em inglês de alguns vilões dos Vingadores 
avengers_villains = ['Loki', 'Ultron', 'Grandmaster', 'Living Laser', 'Red Skull', 'Super-Adaptoid', 'Crossbones', 'Madame Masque', 'Beyonder', 'Absorbing Man', 'M.O.D.O.K.', 'Lethal Legion', 'Kang', 'Sinister Six', 'Rhino', 'The Hood', 'Grim Reaper', 'Masters of Evil', 'Skrulls', 'Hela', 'Taskmaster', 'Korvac', 'Juggernaut', 'Klaw', 'A.I.M.', 'U-Foes', 'Thanos', 'Blob']




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

# Lista de codinomes em inglês de alguns heróis dos X-Men 
xmen_heroes = ['Iceman', 'Surge', 'Sunspot', 'Hellion', 'Wolverine', 'Marrow', 'Cannonball', 'Chamber', 'Deadpool', 'Doop', 'Prodigy', 'Strong Guy', 'Jubilee', 'Psylocke', 'Polaris', 'Professor X', 'Hope Summers', 'Storm', 'Emma Frost', 'Forge', 'Multiple Man', 'Bishop', 'Wolfsbane', 'Cypher', 'Warpath', 'Havok', 'Beast', 'Cyclops', 'Cable', 'X-23', 'Longshot', 'Jean Grey', 'Shadowcat', 'Dust', 'Sage', 'Shatterstar', 'Colossus', 'Archangel', 'Anole', 'Fantomex', 'Gambit', 'Rogue', 'Nightcrawler', 'Karma', 'Pixie', 'Elixir', 'Feral', 'Rockslide', 'Domino']



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


chacter_df = pd.DataFrame(columns=['ID', 'Name', 'Comics', 'Series', 'Events', 'Stories'])


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


marvel_all_characters_df = get_character(marvel_all_characters)

# funcao para juntas listas
def joing_teams(h, v):
    new_c = []
    new_c.append(v)
    new_c.append(h)
    return new_c    



villains_team = joing_teams(avengers_villains, xmen_villains)


heroes_team = joing_teams(xmen_heroes, avengers_heroes)


marvel_char = joing_teams(marvel_villains, marvel_heroes)

# funcao para classificar os personagens das listas de herois
def add_class_hero(x):
    char_ = {'Avengers':[], 'X-Men':[],'X-Men-Avengers':[] }
    char_['Avengers'] = x[0]
    char_['X-Men'] = x[1]
    char_['X-Men-Avengers'] = list(set(x[0]).intersection(set(x[1])))
    return char_



# funcao para classificar os personagens das listas de viloes

def add_class_villain(x):
    char_ = {'Villain_Avengers':[], 'Villain_X-Men':[]}
    char_['Villain_X-Men'] = x[0]
    char_['Villain_Avengers'] = x[1] 
    return char_


class_hero = add_class_hero(heroes_team)

class_villains = add_class_villain(villains_team)

# dicionario recebendo as listas ja classificadas
class_marvel = class_villains.copy()
class_marvel.update(class_hero)
class_marvel 


# funcao para implementar a coluna Class no dataframe ja existente
def transfer_class_df(x):
    for key, value in class_marvel.items():
        if x in value:
            return key


marvel_all_characters_df["Class"] = marvel_all_characters_df["Name"].apply(transfer_class_df)



# funcao que filtra coluna por valor 
    
def sort_one_columns(df, column, column_value):
    sort = df[df[column] == column_value].drop_duplicates()
    return sort


# funcao que filtra uma coluna por diferentes valores 
    
def sort_two_columns(df, column, column_one_value, column_two_value):
    sort = df[(df[column] == column_one_value) | (df[column] == column_two_value)].drop_duplicates()
    return sort


# funcao para aplicar uma condicional pegando os 5 maiores valores de uma coluna 
    
def add_conditial(variable, principal_column, reference_column):
    cond = variable.nlargest(10, principal_column)[[reference_column, principal_column]].drop_duplicates()
    return cond


# funcao filtra as colunas do dataframe e prepara-la pra criar um grafico
def Filter_comic_class(conditional, reference_column, principal_column):
    filter_ = (
    conditional.groupby([reference_column, principal_column])
    .size()
    .reset_index(name='Count')
    .sort_values(principal_column, ascending=True)
    .drop_duplicates(reference_column)
    )
    return filter_
    

# funcao que recebe valores para criar um grafico com matplotlib
def visual_plot(variable, x_column, y_column, x_lable, y_lable, title ):
    sns.barplot(x=x_column, y=y_column, data=variable, palette="Blues")
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.savefig(f'images/test-{title}.jpg', format='jpg')
    plt.show()


conditional_5 = sort_two_columns(marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')



top_comics_avengers_world = add_conditial(conditional_5, 'Comics', 'Name')



top_8_avengers_world = Filter_comic_class(top_comics_avengers_world, 'Name', 'Comics')



visual_plot(top_8_avengers_world, "Name", "Comics", "Name", "Number of Comics", "The Top 10 in Avenger's world with more comics" )


conditional_10 = sort_two_columns(marvel_all_characters_df, 'Class', 'X-Men', 'Villain_X-Men')



top_comics_xmen_world = add_conditial(conditional_10, 'Comics', 'Name')



top_10_xmen_world = Filter_comic_class(top_comics_xmen_world, 'Name', 'Comics')


visual_plot(top_10_xmen_world, "Name", "Comics", "Name", "Number of Comics", "The Top 10 in X-men's world with more comics" )


# funcao que recebe uma coluna e duas variaveis removendo os valores duplicados e devolve os 20 melhores personagens
def add_conditial_20(variable, principal_column, reference_column):
    cond = variable.nlargest(20, principal_column)[[reference_column, principal_column]].drop_duplicates()
    return cond


top_comics_marvel_world = add_conditial_20(marvel_all_characters_df, 'Comics', 'Name')



top_marvels_world = Filter_comic_class(top_comics_marvel_world, 'Name', 'Comics')



visual_plot(top_marvels_world, "Name", "Comics", "Name", "Number of Comics", "The Top 20 in Marvel's world with more comics" )

# funcao que recebe uma coluna e duas variaveis da mesmas coluna removendo os valores duplicados

def sort_two_columns_(df, column, column_one_value, column_two_value):
    sort = df[(df[column] == column_one_value) | (df[column] == column_two_value)].drop_duplicates()
    return sort


# Calcular a porcentagem de Vingadores em relação ao total
total_avengers_comics_ = sort_two_columns_(marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')
total_xmen_comics_ = sort_two_columns_(marvel_all_characters_df, 'Class', 'X-Men', 'Villain_X-Men')


percentage_avengers = (total_avengers_comics_['Comics'].sum() / (total_avengers_comics_['Comics'].sum() + total_xmen_comics_['Comics'].sum())) * 100

print(f"A porcentagem de comics dos Vingadores em relação ao total é: {percentage_avengers:.2f}%")


result_df = pd.DataFrame({'Equipe': ['Vingadores'], 'Porcentagem': [percentage_avengers]})


percentage_avengers = (total_avengers_comics_['Comics'].sum() / (total_avengers_comics_['Comics'].sum() + total_xmen_comics_['Comics'].sum())) * 100
percentage_xmen = 100 - percentage_avengers  # Porcentagem dos X-Men


# Criar DataFrame com os resultados
result_df = pd.DataFrame({'Class': ['Avengers', 'X-Men'], 'Percentage': [percentage_avengers, percentage_xmen]})
print(result_df)


visual_plot(result_df, "Class", "Percentage", "Class", "Percentage", 'Percentage of Avengers and X-Men Comics in Relation to the Total')


perc = result_df['Percentage']
perc
lab = result_df['Class']


perc.plot.pie(autopct="%.1f%%",labels=lab, textprops={'fontsize':14}, colors=sns.color_palette('Blues'))



def build_dataframe (df):
    # 0. Get time
    ts = int(time.time())
    
    # 3. Export
    name = f"marvel-{ts}.csv"
    df.to_csv(f"data/{name}", index=False)
    
    return df

build_dataframe (marvel_all_characters_df)