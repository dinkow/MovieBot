import discord
import handler
import roles

ADD = 'add'
VOTE = 'vote'
REMOVE = 'remove'
LIST = 'list'
VOTE_LIST = 'vlist'
CLEAR_LIST = 'clear'
RANDOMIZE = 'random'
HELP = 'help'

async def handle_response(message) -> str:
    p_message = message.content.lower()
    admin = roles.check_admin(message.author)

    if p_message[:len(ADD)] == ADD:
        await message.delete()
        return handler.add_movie(message)

    elif p_message[:len(VOTE)] == VOTE:
        await message.delete()
        return handler.vote_movie(message)

    elif p_message[:len(REMOVE)] == REMOVE:
        return handler.remove_movie(message)

    elif p_message[:len(LIST)] == LIST:
        return handler.list_movies()
    
    elif p_message[:len(VOTE_LIST)] == VOTE_LIST and admin:
        return handler.vote_list()

    elif p_message[:len(CLEAR_LIST)] == CLEAR_LIST and admin:
        return handler.clear_list()
    
    elif p_message[:len(RANDOMIZE)] == RANDOMIZE and admin:
        return handler.randomize()

    elif p_message[:len(HELP)] == HELP:
        return handler.help(admin)
