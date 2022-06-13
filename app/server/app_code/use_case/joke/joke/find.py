from app_code.model.joke.joke_model import Joke
from app_code.repository.joke.joke_repository import update, find_or_fail

def handler(joke_id):

    joke = find_or_fail(joke_id)

    return joke.as_dict()