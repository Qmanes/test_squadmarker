from app_code.model.joke.joke_model import Joke
from app_code.repository.joke.joke_repository import all as all_list

def handler():

    jokes = all_list()

    return list(map(lambda joke: joke.as_dict(), jokes))
