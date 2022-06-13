from app_code.repository.mariadb.Execute import Execute
from app_code.model.joke.joke_model import Joke

TABLE = "jokes"

EXECUTE = Execute(TABLE, Joke, "Joke")

def save(joke):

    return EXECUTE.save(joke)

def update(joke):
    
    return EXECUTE.update(joke)

def find_or_fail(joke_id):

   return EXECUTE.find_or_fail(joke_id)

def delete(joke):

    return EXECUTE.delete(joke)

def all():

    return EXECUTE.all()