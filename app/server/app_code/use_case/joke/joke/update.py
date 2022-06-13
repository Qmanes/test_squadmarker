from app_code.model.joke.joke_model import Joke
from app_code.repository.joke.joke_repository import update, find_or_fail

def handler(joke_param):

    joke = find_or_fail(joke_param.get("number"))

    joke.update(joke_param.get("joke_new"))

    joke_updated = update(joke)

    return joke_updated.as_dict()