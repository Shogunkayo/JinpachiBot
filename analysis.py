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
    request = request.replace('A', '[AÀÁÂÃÄÅÆàáâãäåæĀāĂăĄąǍǎǞ₳ΆȀȦȺȧȁȂȃǟǠǡǢǣ]')
    request = request.replace('C', '[ÇCçĆćĈĉĊċČč]')
    request = request.replace('D', '[DÐĐĎďĐđ]')
    request = request.replace('E', '[EÉÈÊËèéêëĒēĔĕĖėĘęĚě]')
    request = request.replace('G', '[GĜĝĞĠġĢģ]')
    request = request.replace('H', '[HĤĥĦħ]')
    request = request.replace('I', '[IÌÍÎÏìíîïĨĩĪīĬĭĮįİıĲĳ]')
    request = request.replace('J', '[JĴĵ]')
    request = request.replace('K', '[KĶķĸ]')
    request = request.replace('L', '[LĹĺĻļĽľĿŀŁł]')
    request = request.replace('N', '[NŃńŅņŇňŉŊŋ]')
    request = request.replace('O', '[OÒÓÔÕÖØòóôõöŌōŎŏŐő]')
    request = request.replace('R', '[RŔŕŖŗŘř]')
    request = request.replace('S', '[SšŠŚśŜŝŞşŠš]')
    request = request.replace('T', '[TŢţŤťŦŧ]')
    request = request.replace('U', '[UÙÚÛÜùúûüŰűŲųŨũŪūŬŭŮůŰűŲųǓǔǕǖǗǘǙǚǛǜ]')
    request = request.replace('W', '[WŴŵ]')
    request = request.replace('Y', '[YŶŷŸ]')
    request = request.replace('Z', '[ZŹźŻżŽž]')
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

if __name__ == '__main__':
    
    temp = search_player('MESSi')
    print(temp)
    temp = [temp[i:i + 4] for i in range(0, len(temp), 4)]
    for i in range(len(temp)):
        output = ">>>\n----------------------------------------------------------\n"
        for j in temp[i]:
            if(len(j[0]) < 20):
                j[0] = j[0].ljust(20)
            else:
                j[0] = j[0][:17] + '...'
            
            if(len(j[2]) < 20):
                j[2] = j[2].ljust(20)
            else:
                j[2] = j[2][:17] + '...'
            
            if(len(j[3]) < 20):
                j[3] = j[3].ljust(20)
            else:
                j[3] = j[3][:17] + '...'

            if(len(j[4]) < 20):
                j[4] = j[4].ljust(20)
            else:
                j[4] = j[4][:17] + '...'

            if(j[7] == -1):
                j[7] = '-1     '

            output += f"| + Name:   {j[0]}  + Position: {j[1]} \t |\n| + Club:   {j[2]}  + Ovr Rating: {j[5]} \t |\n| + Nation: {j[3]}  + Base Rating: {j[6]} \t |\n| + League: {j[4]}  + Price: {j[7]} \t |\n|--------------------------------------------------------|\n"
        temp[i] = output

    for i in temp:
        print(i,'\n\n')
    

