from app_code.model.joke.joke_model import Joke
from app_code.repository.joke.joke_repository import save

def handler(joke_param):


    joke = Joke(**joke_param)

    joke.save()

    joke_save = save(joke)

    return joke_save.as_dict()