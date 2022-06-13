from flask import request
from flask_restful import Resource
from app_code.service.utils.response import try_catch
from app_code.exception.basic_exception import NotFoundException
from app_code.use_case.joke.joke.search import handler as search_joke
from app_code.use_case.joke.joke.save import handler as save_joke
from app_code.use_case.joke.joke.update import handler as update_joke
from app_code.use_case.joke.joke.delete import handler as delete_joke
from app_code.use_case.joke.joke.find import handler as find_joke
from app_code.use_case.joke.joke.all import handler as all_joke

class SearchJoke(Resource):
    
    def get(self):
        
        def handler():

            msg = "joke search"

            param = get_param("param")

            param = param.capitalize() if param else None

            return search_joke(param), msg

        return try_catch(handler)

class FindJoke(Resource):
    
    def get(self):
        
        def handler():

            msg = "joke find"

            number = get_param("number")

            number = request.args.get('number')

            return find_joke(number), msg

        return try_catch(handler)

class AllJoke(Resource):
    
    def get(self):
        
        def handler():

            msg = "joke all"

            return all_joke(), msg

        return try_catch(handler)

class SaveJoke(Resource):
    
    def post(self):
        
        def handler():

            msg = "joke save"

            param = request.get_json()

            return save_joke(param), msg

        return try_catch(handler)

class UpdateJoke(Resource):
    
    def put(self):
        
        def handler():

            msg = "joke update"

            param = request.get_json()

            return update_joke(param), msg

        return try_catch(handler)

class DeleteJoke(Resource):
    
    def delete(self):
        
        def handler():

            msg = "joke Delete"

            param = request.get_json()

            return delete_joke(param), msg

        return try_catch(handler)

def get_param(param_name):

    param = request.args.get(param_name)

    if param_name in request.args and not param:
        
        raise NotFoundException(param_name.capitalize())

    return param