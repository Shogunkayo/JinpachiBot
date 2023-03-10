import pandas as pd
import numpy as np
import re

df = pd.read_csv('cards')
df = df.applymap(lambda x: x.upper() if type(x) == str else x)
df = df.drop('no', axis=1)

'''
formations = [  {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'CM' : '', 'CM': '', 'LM': '', 'CAM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'CM' : '', 'CM': '', 'LM': '', 'CF': '', 'RM': '', 'ST': '', 'CF': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'CM' : '', 'CM': '', 'LM': '', 'CDM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'CM' : '', 'CM': '', 'LM': '', 'LW': '', 'RM': '', 'ST': '', 'RW': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'CDM' : '', 'CAM': '', 'LM': '', 'CAM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'LM': '', 'CAM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CM': '', 'CAM': '', 'CM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'LM': '', 'CM': '', 'RM': '', 'CM': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CDM': '', 'CAM': '', 'CAM': '', 'CAM': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CDM': '', 'CAM': '', 'RM': '', 'LM': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CDM': '', 'CAM': '', 'CAM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'LW': '', 'RW': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'CM': '', 'CAM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'LM': '', 'CAM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'LM': '', 'CM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'CM': '', 'CF': '', 'CF': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'CM': '', 'LW': '', 'RW': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CM': '', 'CM': '', 'LW': '', 'RW': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CDM': '', 'CM': '', 'LW': '', 'RW': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'CAM': '', 'LW': '', 'RW': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CM': '', 'CM': '', 'LW': '', 'RW': '', 'CF': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'LM': '', 'CF': '', 'RM': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'LM': '', 'CAM': '', 'RM': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'LM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CDM': '', 'CDM': '', 'LM': '', 'RM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'LM': '', 'RM': '', 'CAM': '', 'CAM': '', 'ST': ''},
                {'GK' : '', 'LB' : '', 'CB' : '', 'CB' : '', 'RB' : '', 'CM': '', 'CM': '', 'CM': '', 'LM': '', 'RM': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'LWB' : '', 'RWB': '', 'CM': '', 'CM': '', 'CAM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'LWB' : '', 'RWB': '', 'CM': '', 'CM': '', 'LW': '', 'RW': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'LWB' : '', 'RWB': '', 'CDM': '', 'CM': '', 'CM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'LWB' : '', 'RWB': '', 'CM': '', 'CM': '', 'CAM': '', 'ST': '', 'ST': ''},
                {'GK' : '', 'CB' : '', 'CB' : '', 'CB' : '', 'LWB' : '', 'RWB': '', 'CM': '', 'CM': '', 'LM': '', 'RM': '', 'ST': ''},
]
'''

    

def format_string(request):
    request = request.replace('A', '[A???????????????????????????????????????????????????????????????????????????]')
    request = request.replace('C', '[??C??????????????????]')
    request = request.replace('D', '[D????????????]')
    request = request.replace('E', '[E????????????????????????????????????]')
    request = request.replace('G', '[G??????????????]')
    request = request.replace('H', '[H????????]')
    request = request.replace('I', '[I????????????????????????????????????????]')
    request = request.replace('J', '[J????]')
    request = request.replace('K', '[K??????]')
    request = request.replace('L', '[L????????????????????]')
    request = request.replace('N', '[N??????????????????]')
    request = request.replace('O', '[O??????????????????????????????????]')
    request = request.replace('R', '[R????????????]')
    request = request.replace('S', '[S????????????????????]')
    request = request.replace('T', '[T????????????]')
    request = request.replace('U', '[U????????????????????????????????????????????????????????????????????]')
    request = request.replace('W', '[W????]')
    request = request.replace('Y', '[Y??????]')
    request = request.replace('Z', '[Z????????????]')
    return request

def search_player(name) -> str:
    name = format_string(name)
    return (df.loc[df['name'].str.contains(name, flags= re.IGNORECASE, regex= True)].sort_values('base_ratings', ascending=False)).to_numpy().tolist()

def search_nation(nation) -> str:
    nation = format_string(nation)
    return (df.loc[df['nation'].str.contains(nation, flags= re.IGNORECASE, regex= True)].sort_values('base_ratings', ascending=False)).to_numpy().tolist()

def search_club(club) -> str:
    club = format_string(club)
    return (df.loc[df['club'].str.contains(club, flags= re.IGNORECASE, regex= True)].sort_values('base_ratings', ascending=False)).to_numpy().tolist()

def search_league(league) -> str:
    league = format_string(league)
    return (df.loc[df['league'].str.contains(league, flags= re.IGNORECASE, regex= True)].sort_values('base_ratings', ascending=False)).to_numpy().tolist()

def search_position(position) -> str:
    return (df.loc[df['position'].str.contains(position, flags= re.IGNORECASE, regex= True)].sort_values('base_ratings', ascending=False)).to_numpy().tolist()

def best_nation(nation) -> str:
    nation = format_string(nation)
    temp = df.loc[df['nation'].str.contains(nation, flags= re.IGNORECASE, regex= True)].sort_values('base_ratings', ascending=False)
    
    if(temp.shape[0] > 500):
        temp = temp.loc[temp['base_ratings'] > 400]
    print(temp.shape[0])
    gk = temp.loc[temp['position'] == 'GK']
    temp = temp.loc[temp['position'] != 'GK']
    print(temp.shape[0])
    print(gk.shape[0])

if __name__ == '__main__':
    
    temp = best_nation('SPAIN')
    