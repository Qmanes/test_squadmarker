import random
from app_code.repository.mock.joke_type_mock import all_joke_type, find_joke_type
from app_code.service.utils.petition import get as get_petition

def handler(param = None):

    
    joke_type = get_joke_type(param)

    joke_response = get_petition(joke_type.get("endpoint"))

    return joke_response.get(joke_type.get("key"))


def get_joke_type(param = None):

    joke_type = None

    if (param):

        joke_type = find_joke_type(param)

    else:

        joke_type_list = all_joke_type()

        joke_type = random.choice(joke_type_list)

    return joke_type