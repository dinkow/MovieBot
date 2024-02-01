def handle_response(message) -> str:
    p_message = message.lower()

    if p_message[:3] == 'rec':
        return 'rec'
    
    elif p_message[:4] == 'vote':
        return 'vote'
    
    elif p_message[:4] == 'list':
        return 'list'
    
    elif p_message[:4] == 'help':
        return 'help'
    