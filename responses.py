import random
import analysis

def handle_response(message) -> str:
    request = message.upper()

    if(request == 'HELLO'):
        return 'Hey there!'
    
    if(request == 'ROLL'):
        return str(random.randint(1, 100))
    
    if(request[0] == 'P' or request[:6] == 'PLAYER'):
        try:
            if(request[1] == ' '):
                request = request[2:]
                request = request.strip()
            elif(request[6] == ' '):
                request = request[7:]
                request = request.strip()
            else:
                return 'Invalid format'
        except:
            return 'Invalid format'

        if(len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_player(request)[:1990] + '```'

    if(request[0] == 'N' or request[:6] == 'NATION'):
        try:
            if(request[1] == ' '):
                request = request[2:]
                request = request.strip()
            elif(request[6] == ' '):
                request = request[7:]
                request = request.strip()
            else:
                return 'Invalid format'
        except:
            return 'Invalid format'

        if(len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_nation(request)[:1990] + '```'

    
    if(request[0] == 'C' or request[:6] == 'CLUB'):
        try:
            if(request[1] == ' '):
                request = request[2:]
                request = request.strip()
            elif(request[6] == ' '):
                request = request[7:]
                request = request.strip()
            else:
                return 'Invalid format'
        except:
            return 'Invalid format'

        if(len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_club(request)[:1990] + '```'
    
    if(request[0] == 'L' or request[:6] == 'LEAGUE'):
        try:
            if(request[1] == ' '):
                request = request[2:]
                request = request.strip()
            elif(request[6] == ' '):
                request = request[7:]
                request = request.strip()
            else:
                return 'Invalid format'
        except:
            return 'Invalid format'

        if(len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_league(request)[:1990] + '```'

    if(request[0] == 'POS' or request[:6] == 'POSITION'):
        try:
            if(request[1] == ' '):
                request = request[2:]
                request = request.strip()
            elif(request[6] == ' '):
                request = request[7:]
                request = request.strip()
            else:
                return 'Invalid format'
        except:
            return 'Invalid format'

        if(len(request) > 40):
            return 'Lock off'
        
        return '```' + analysis.search_position(request)[:1990] + '```'

    if(request == 'help'):
        return '>>> Teehee'
    
    return 'I have no response for this'