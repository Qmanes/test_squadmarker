from app_code.exception.basic_exception import NotFoundException
def all_joke_type():

    return [
        {
            "uid": 1,
            "name": "Chuck Norris Jokes",
            "endpoint": "https://api.chucknorris.io/jokes/random",
            "param": "Chuck",
            "key": "value",
            "status": "active",
            "created_at": "234",
            "updated_at": None,
            "deleted_at": None
        },
        {
            "uid": 2,
            "name": "I can haz dad joke",
            "endpoint": "https://icanhazdadjoke.com/",
            "param": "Dad",
            "key": "joke",
            "status": "active",
            "created_at": "234",
            "updated_at": None,
            "deleted_at": None
        }
    ]

def find_joke_type(param):

    joke_type = [joke_type for joke_type in  all_joke_type() if joke_type.get("param").capitalize() == param]
    
    if not joke_type:

        raise NotFoundException(param)

    return joke_type[0]