import json
import random

FILENAME = 'movies.json'

def open_json():
    with open(FILENAME, "r") as json_file:
        existing_data = json.load(json_file)
    return existing_data

def write_json(existing_data):
    with open(FILENAME, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)


def add_movie(message) -> str:
    movie = str(message.content[4:])
    user = str(message.author)

    existing_data = open_json()

    for recommendation in existing_data:
        if recommendation.get("user") == user:
            return "`You've already added a movie recommendation.`"

    for recommendation in existing_data:
        if recommendation.get("movie") == movie:
            return '`Movie ' + movie + ' already added.`'

    new_item = {
        "movie": movie,
        "user": user,
        "voters": []
    }

    existing_data.append(new_item)

    write_json(existing_data)

    return '`Movie '+ movie +' added!`'


def vote_movie(message) -> str:
    movie = str(message.content[5:])
    user = str(message.author)

    existing_data = open_json()

    for recommendation in existing_data:
        if recommendation.get("movie") == movie:
            for second in existing_data:
                if user in second["voters"]:
                    second["voters"].remove(user)
            recommendation["voters"].append(user)

            write_json(existing_data)

            return '`Vote updated.`'

    return '`Movie not found. Please check spelling.`'


def remove_movie(message) -> str:
    user = str(message.author)

    existing_data = open_json()

    for recommendation in existing_data:
        if recommendation.get("user") == user:
            existing_data.remove(recommendation)

            write_json(existing_data)

            return '`Your movie recommendation was removed.`'
        
    return '`You dont have a movie recommendation.`'


def list_movies() -> str:
    movie_list = ''

    existing_data = open_json()

    for recommendation in existing_data:
        movie_list = movie_list + recommendation.get("movie") + '\n'

    if movie_list == '':
        return '`There are no movie recommendations right now.`'
    else:
        return '`' + movie_list + '`'


def vote_list() -> str:
    movie_votes = ''

    existing_data = open_json()

    for recommendation in existing_data:
        voter_count = len(recommendation["voters"])
        movie_votes += recommendation.get("movie") + f': {voter_count}\n'

    if movie_votes == '':
        return '`There are no movie recommendations right now.`'
    else:
        return '`' + movie_votes + '`'


def clear_list() -> str:
    write_json([])

    return '`Movie list has been cleared.`'

def randomize() -> str:
    existing_data = open_json()
    
    randomize_data = random.sample(existing_data, k=3)

    write_json(randomize_data)

    return 'List randomized.'


def help(admin) -> str:
    help_text = 'MovieBot commands\n`-add `*`movie name`*`:` add a movie to the list\n`-vote `*`movie name`*`:` vote for a specific movie\n`-list:` see current movie recommendations\n`-remove:` removes your movie recommendation'
    if admin:
        help_text += '\n\nadmin commands\n`-vlist:` see current movie recommendations as well as votes\n`-random:` randomly choose 3 movies and delete the rest\n`-clear:` clears the movie list'
    return help_text