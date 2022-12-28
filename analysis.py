import pandas as pd
import numpy as np
import re

df = pd.read_csv('cards')
df = df.applymap(lambda x: x.upper() if type(x) == str else x)

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
    print(len(search_position('st')))