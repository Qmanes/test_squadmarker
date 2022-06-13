import requests
import json
from validator_collection import validators, checkers
from app_code.exception.basic_exception import UrlNotValidException

headers = {'Accept': 'application/json'}

def get(url):

    if not checkers.is_url(url):

        raise UrlNotValidException(url)

    r = requests.get(url, headers=headers)
    
    return r.json() 
    #requests.exceptions.MissingSchema