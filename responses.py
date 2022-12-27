import random

def handle_response(message) -> str:
    request = message.lower()

    if(request == 'hello'):
        return 'Hey there!'
    
    if(request == 'roll'):
        return str(random.randint(1, 6))
    
    if(request == '!help'):
        return '`Testing`'
    
    return 'I have no response for this'
