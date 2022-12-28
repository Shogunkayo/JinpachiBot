import discord

import random
import analysis

def clean_request(request) -> str:
    if(request[1] == ' '):
        request = request[2:]
        request = request.strip()
    elif(request[6] == ' '):
        request = request[7:]
        request = request.strip()
    else:
        request = '0'    
    
    return request

def handle_response_misc(message):
    request = message.upper()

    if(request == 'HELLO'):
        return 'Hey there!'
    
    if(request == 'ROLL'):
        return str(random.randint(1, 100))

    if(request == 'help'):
        return '>>> Teehee'
    
    return 'I have no response for this'


def handle_response_search(message):
    request = message.upper()

    if(request[0] == 'P' or request[:6] == 'PLAYER'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
        
        return '```' + str(analysis.search_player(request)) + '```'


    if(request[0] == 'N' or request[:6] == 'NATION'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
    
        return '```' + analysis.search_nation(request) + '```'

    
    if(request[0] == 'C' or request[:6] == 'CLUB'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'

        return '```' + analysis.search_club(request)[:1990] + '```'
    

    if(request[0] == 'L' or request[:6] == 'LEAGUE'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_league(request)[:1990] + '```'


    if(request[0] == 'POS' or request[:6] == 'POSITION'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_position(request)[:1990] + '```'

'''
>>>
---------------------------------------------
| + Name: Lionel Messi  + Position: CF      |
| + Club: Paris SG      + Ovr Rating: 94    |
| + Nation: Argentina   + Base Rating: 477  |
| + League: Ligue 1     + Price: 1935000    |
| ------------------------------------------|
| + Name: Lionel Messi  + Position: CF      |
| + Club: Paris SG      + Ovr Rating: 94    |
| + Nation: Argentina   + Base Rating: 477  |
| + League: Ligue 1     + Price: 1935000    |
| ------------------------------------------|
| + Name: Lionel Messi  + Position: CF      |
| + Club: Paris SG      + Ovr Rating: 94    |
| + Nation: Argentina   + Base Rating: 477  |
| + League: Ligue 1     + Price: 1935000    |
| ------------------------------------------|
| + Name: Lionel Messi  + Position: CF      |
| + Club: Paris SG      + Ovr Rating: 94    |
| + Nation: Argentina   + Base Rating: 477  |
| + League: Ligue 1     + Price: 1935000    |
---------------------------------------------
'''