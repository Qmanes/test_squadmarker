import traceback
import json

from flask import request, jsonify, make_response
from app_code.exception.basic_exception import NotFoundException, LiteralFormatException
from requests.exceptions import ConnectionError
def try_catch(action):

    status_code = 200

    try:
         response, msg = action()

         res = get_response(data = response, status_code = status_code, msg = msg)   

    except NotFoundException as error:
    
        status_code = 404
        res = error_response(error, status_code)

    except LiteralFormatException as error:
    
        status_code = 402
        res = error_response(error, status_code)

    except ValueError as error:

        status_code = 406
        res = error_response("Error: value isn't type int", status_code)

    except ConnectionError as error:

        status_code = 400
        res = error_response("Error Failed to establish a connection", status_code)

    except Exception as error:

        status_code = 500
        res = error_response(error, status_code)      

    finally:

        response = make_response(json.dumps(res), status_code)
        response.headers['mimetype'] = 'application/json'
        return response


def error_response(error, status_code):

    traceback.print_exc()

    return get_response(status_code = status_code, msg = str(error))

def get_response(status_code, msg, data = None,):

    return {
            "data": data,
            "status": status_code,
            "msg": msg
        }