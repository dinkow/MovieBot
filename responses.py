def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '-m hello':
        return 'Hey there!'
    
    