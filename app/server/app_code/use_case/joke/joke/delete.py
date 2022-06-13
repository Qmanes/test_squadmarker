
from app_code.repository.joke.joke_repository import delete, find_or_fail

def handler(joke_param):

    joke = find_or_fail(joke_param.get("number"))

    joke.delete()

    delete(joke)

    return "Delete success"