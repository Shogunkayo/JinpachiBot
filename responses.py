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

def format_space(text):
    if(len(text) < 20):
        return text.ljust(20)
    
    return text[:17] + '...'

def format_response(response):
    response = [response[i:i+4] for i in range(0, len(response), 4)]
    
    for chunk in range(len(response)):
        output = "``` \n---------------------------------------------------------\n"

        for i in response[chunk]:
            i[0] = format_space(i[0])
            i[2] = format_space(i[2])
            i[3] = format_space(i[3])
            i[4] = format_space(i[4])
            i[1] = i[1].ljust(7)
            i[5] = str(i[5]).ljust(7)
            i[6] = str(i[6]).ljust(7)
            i[7] = str(i[7]).ljust(7)

            output += f"|+ Name:   {i[0]}  + Position   : {i[1]} |\n|+ Club:   {i[2]}  + Ovr Rating : {i[5]} |\n|+ Nation: {i[3]}  + Base Rating: {i[6]} |\n|+ League: {i[4]}  + Price      : {i[7]} |\n|-------------------------------------------------------|\n"

        response[chunk] = output + '\n```'

    return response

def handle_response_help():
    return '```\nJinpachiBot - Help\nIt’s Simple Really\n\n🔍 Search -> Search for players, sorted based on total base ratings\n🏳️ Misc -> Miscellaneous commands```'

def handle_response_misc(message, client):
    request = message.upper()

    if(request == 'HELLO'):
        return 'Hello, diamonds in the rough'
    
    if(request == 'ROLL'):
        return str(random.randint(1, 100))

    if(request == 'PING'):
        return f'Pong! {round (client.latency * 1000)}ms'

    return 'I have no response for this'


def handle_response_search(message):
    request = message.upper()


    if(request[:3] == 'POS' or request[:6] == 'POSITION'):
        if(request[3] == ' '):
            request = request[4:]
            request.strip()
        elif(request[8] == ' '):
            request = request[9:]
            request.strip()
        else:
            request = '0'

        if(request[:6] == 'ATTACK'):
            request = 'ST|CF|LW|RW'
        
        if(request[:7] == 'DEFENCE'):
            request = 'CB|LB|RB|LWB|RWB'
        
        if(request[:8] == 'MIDFIELD'):
            request = 'CM|CAM|CDM|LM|RM'

        if(request == '0' or len(request) > 40):
            return 'Lock off'
        
        response = analysis.search_position(request)
        if(len(response) == 0):
            return ['Valid positions are\n```\nattack -> LW ST CF RW\nmidfield -> LM CAM CM CDM RM\ndefence -> LB LWB CB RB RWB\nGK```']
        
        return format_response(response) 


    if(request[0] == 'P' or request[:6] == 'PLAYER'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
        
        return format_response(analysis.search_player(request)) 


    if(request[0] == 'N' or request[:6] == 'NATION'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
    
        return format_response(analysis.search_nation(request)) 

    
    if(request[0] == 'C' or request[:4] == 'CLUB'):
        if(request[1] == ' '):
            request = request[2:]
            request.strip()
        elif(request[4] == ' '):
            request = request[5:]
            request.strip()
        else:
            request = '0'


        if(request == '0' or len(request) > 40):
            return 'Lock off'

        return format_response(analysis.search_club(request)) 
    

    if(request[0] == 'L' or request[:6] == 'LEAGUE'):
        request = clean_request(request)
        if(request == '0' or len(request) > 40):
            return 'Lock off'
        
        return format_response(analysis.search_league(request)) 

def handle_anime_response(request) -> str:
    return 'HEHE'