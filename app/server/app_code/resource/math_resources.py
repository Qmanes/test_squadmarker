from flask import request
from flask_restful import Resource
from app_code.service.utils.response import try_catch
from app_code.use_case.math.lowest_common_multiple import handler as lowest_common_multiple
from app_code.use_case.math.add_one import handler as add_one
from app_code.exception.basic_exception import NotFoundException

class Math(Resource):
    
    def get(self):
        
        def handler():

            msg = "math"

            if "numbers" in request.args:
                
                return lowest_common_multiple(request.args.get("numbers")), msg

            if "number" in request.args:

                return add_one(request.args.get("number")), msg

            raise NotFoundException(param_name.capitalize)

        return try_catch(handler)       