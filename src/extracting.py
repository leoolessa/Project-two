import pandas as pd
from marvel import Marvel



# Avengers hero list:
avengers_heroes = [
    'Scarlet Witch', 'Wasp', 
    'Black Widow', 'Hulk', 
    'Hawkeye', 'Vision', 
    'Falcon', 'Luke Cage', 
    'Jessica Jones', 'Black Panther', 
    'Iron Man', 'Wolverine', 
    'Storm', 'Iron Patriot', 
    'Doctor Strange', 'Thor', 
    'Daredevil','Captain America'
    ]


# Avengers Villains list:
avengers_villains = [
    'Loki', 'Ultron', 
    'Grandmaster', 'Living Laser', 
    'Red Skull', 'Super-Adaptoid', 
    'Crossbones', 'Madame Masque', 
    'Beyonder', 'Absorbing Man', 
    'M.O.D.O.K.', 'Lethal Legion', 
    'Kang', 'Sinister Six', 
    'Rhino', 'The Hood', 
    'Grim Reaper', 'Masters of Evil', 
    'Skrulls', 'Hela', 
    'Taskmaster', 'Korvac', 
    'Juggernaut', 'Klaw', 
    'A.I.M.', 'U-Foes', 
    'Thanos', 'Blob'
    ]


# X-Men Villain list:
xmen_villains = [
  'Magneto', 'The Hand',
  'Pyro', 'Mystique',
  'Gideon', 'Lady Deathstrike',
  'Sabretooth', 'Sebastian Shaw',
  'Shadow King', 'Apocalypse',
  'Exodus', 'Onslaught',
  'Emma Frost', 'Avalanche',
  'Silver Samurai', 'Cassandra Nova',
  'Mastermind', 'Master Mold',
  'Dark Phoenix', 'Juggernaut',
  'William Stryker', 'Selene',
  'Omega Red', 'Marauders',
  'Bastion', 'Loki',
  'Ultron', 'Grandmaster',
  'Living Laser', 'Red Skull',
  'Super-Adaptoid', 'Crossbones',
  'Madame Masque', 'Beyonder',
  'Absorbing Man', 'M.O.D.O.K.',
  'Lethal Legion', 'Kang',
  'Sinister Six', 'Rhino',
  'The Hood', 'Grim Reaper',
  'Masters of Evil', 'Skrulls',
  'Hela', 'Taskmaster',
  'Korvac', 'Juggernaut',
  'Klaw', 'A.I.M.',
  'U-Foes', 'Thanos',
  'Blob'
  ]


# X-Men hero list:
xmen_heroes = [
    'Iceman', 'Surge', 
    'Sunspot', 'Hellion', 
    'Wolverine', 'Marrow', 
    'Cannonball', 'Chamber', 
    'Deadpool', 'Doop', 
    'Prodigy', 'Strong Guy', 
    'Jubilee', 'Psylocke', 
    'Polaris', 'Professor X', 
    'Hope Summers', 'Storm', 
    'Emma Frost', 'Forge', 
    'Multiple Man', 'Bishop', 
    'Wolfsbane', 'Cypher', 
    'Warpath', 'Havok', 
    'Beast', 'Cyclops', 
    'Cable', 'X-23', 
    'Longshot', 'Jean Grey', 
    'Shadowcat', 'Dust', 
    'Sage', 'Shatterstar', 
    'Colossus', 'Archangel', 
    'Anole', 'Fantomex', 
    'Gambit', 'Rogue', 
    'Nightcrawler', 'Karma', 
    'Pixie', 'Elixir', 
    'Feral', 'Rockslide', 
    'Domino'
    ]

# All Marvel characters:
marvel_all_characters = [
  'Scarlet Witch', 'Wasp',
  'Black Widow', 'Hulk',
  'Hawkeye', 'Vision',
  'Falcon', 'Luke Cage',
  'Jessica Jones', 'Black Panther',
  'Iron Man', 'Wolverine',
  'Storm', 'Iron Patriot',
  'Doctor Strange', 'Thor',
  'Daredevil', 'Captain America',
  'Iceman', 'Surge',
  'Sunspot', 'Hellion',
  'Wolverine', 'Marrow',
  'Cannonball', 'Chamber',
  'Deadpool', 'Doop',
  'Prodigy', 'Strong Guy',
  'Jubilee', 'Psylocke',
  'Polaris', 'Professor X',
  'Hope Summers', 'Storm',
  'Emma Frost', 'Forge',
  'Multiple Man', 'Bishop',
  'Wolfsbane', 'Cypher',
  'Warpath', 'Havok',
  'Beast', 'Cyclops',
  'Cable', 'X-23',
  'Longshot', 'Jean Grey',
  'Shadowcat', 'Dust',
  'Sage', 'Shatterstar',
  'Colossus', 'Archangel',
  'Anole', 'Fantomex',
  'Gambit', 'Rogue',
  'Nightcrawler', 'Karma',
  'Pixie', 'Elixir',
  'Feral', 'Rockslide',
  'Domino', 'Magneto',
  'The Hand', 'Pyro',
  'Mystique', 'Gideon',
  'Lady Deathstrike', 'Sabretooth',
  'Sebastian Shaw', 'Shadow King',
  'Apocalypse', 'Exodus',
  'Onslaught', 'Emma Frost',
  'Avalanche', 'Silver Samurai',
  'Cassandra Nova', 'Mastermind',
  'Master Mold', 'Dark Phoenix',
  'Juggernaut', 'William Stryker',
  'Selene', 'Omega Red',
  'Marauders', 'Bastion',
  'Loki', 'Ultron',
  'Grandmaster', 'Living Laser',
  'Red Skull', 'Super-Adaptoid',
  'Crossbones', 'Madame Masque',
  'Beyonder', 'Absorbing Man',
  'M.O.D.O.K.', 'Lethal Legion',
  'Kang', 'Sinister Six',
  'Rhino', 'The Hood',
  'Grim Reaper', 'Masters of Evil',
  'Skrulls', 'Hela',
  'Taskmaster', 'Korvac',
  'Juggernaut', 'Klaw',
  'A.I.M.', 'U-Foes',
  'Thanos', 'Blob'
  ]


def get_character(ave, marvel):
    """ summary:
        1. Gets a value from the characters list
        2. Extract the data from API
        3. Return a Dataframe with the data extracted from API
    Args:
        ave:
        Receive a value from a list 
    Returns:
        _type_:
        Return data from API as DataFrame
    """
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


def joing_teams(h, v):
    """ summar:
        1. Gets the value from the lists
        2. Join the values from the list
        3. Return a list with two lists in
    Args:
        h: gets hero list
        v: gets villain list
    Returns:
        Return a list with two lists in
    """
    new_c = []
    new_c.append(v)
    new_c.append(h)
    return new_c 

def add_class_hero(x):
    """summar:
        1. Get the list of hero teams          
        2. Give an attribute to every value from the list: 
            - 'Avengers', 'X-Men','X-Men-Avengers'
        3. Check if the value is in double if it is get the attribute:
            -'X-Men-Avengers'
        4. Return a dict with all the attributed values       
    Args:
        x: Gets the hero list
    Returns:
        Return a dict with all the attributed values
    """
    char_ = {'Avengers':[], 'X-Men':[],'X-Men-Avengers':[] }
    char_['Avengers'] = x[0]
    char_['X-Men'] = x[1]
    char_['X-Men-Avengers'] = list(set(x[0]).intersection(set(x[1])))
    return char_


def add_class_villain(x):
    """summar:
        1. Get the list of villain teams          
        2. Give an attribute to every value from the list: 
            - 'Villain_Avengers', 'Villain_X-Men'
        3. Return a dict with all the attributed values       
    Args:
        x: Gets the hero list
    Returns:
        Return a dict with all the attributed values
    """
    char_ = {'Villain_Avengers':[], 'Villain_X-Men':[]}
    char_['Villain_X-Men'] = x[0]
    char_['Villain_Avengers'] = x[1] 
    return char_


def transfer_class_df(x):
    """summary:
    1. Get a dict
    2. Check every value from the dict to separate the attributed values
    3. Return only the the attributed values

    Args:
        x: Get a dict

    Returns:
        Return only the the attributed values
    """
    for key, value in class_marvel.items():
        if x in value:
            return key


# Calling the function to extract the data
marvel_all_characters_df = get_character(marvel_all_characters)

# Joing all the lists
villains_team = joing_teams(avengers_villains, xmen_villains)
heroes_team = joing_teams(xmen_heroes, avengers_heroes)

# Calling the function add_class
class_hero = add_class_hero(heroes_team)
class_villains = add_class_villain(villains_team)

# Class Marvel
class_marvel = class_villains.copy()
class_marvel.update(class_hero)

# DF receive the attribute value in a new column by the name
marvel_all_characters_df["Class"] = marvel_all_characters_df["Name"].apply(transfer_class_df)
marvel_all_characters_df

