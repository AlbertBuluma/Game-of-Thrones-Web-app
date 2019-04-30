import csv
from config import *

class Characters:
    def __init__(self, name, district, mothers_name, fathers_name, date_registered, episodes_per_season, death_season): # Adding table fields as class fields
        self.name = name
        self.district = district
        self.mothers_name = mothers_name
        self.fathers_name = fathers_name
        self.date_registered = date_registered
        self.episodes_per_season = episodes_per_season
        self.death_season = death_season
        
    def write(self):    #Returns a dictionary with table fields
        return {'name': self.name, 'district': self.district, 'mothers_name': self.mothers_name, 'fathers_name': self.fathers_name, 'date_registered': self.date_registered, 'episodes_per_season': self.episodes_per_season, 'death_season': self.death_season}
             
        
def read_csv_file(file_name):       #Function to read from CSV files
    data = []
    with open(file_name, 'rt') as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            data.append(row)
    return data


def prepare_data():             #Function to manipulate data in CSV variables
    file = read_csv_file(CHARACTERS_PATH)
    episodes_per_season = read_csv_file(EPISODES_PER_SEASON_PATH)
    
    x = []
    
    for row in file:
        name = row.get('name')
        district = row.get('district')
        mothers_name = row.get('mothers name')
        fathers_name = row.get('fathers name')
        date_registered = row.get('date registered')
        character_episodes = []
        death_season = ""
        for appearance in episodes_per_season:
            if appearance.get('user') == name:
                character_episodes.append("%s Episodes in Season %s" % (appearance.get('no of episodes'), appearance.get('season')))
                if int(appearance.get('died in this season')):
                    death_season = appearance.get('season')
                    
        Episodes_per_season = character_episodes
        
        x.append(Characters(name, district, mothers_name, fathers_name, date_registered, Episodes_per_season, death_season))
        
    return x