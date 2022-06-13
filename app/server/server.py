import os
import json
from flask import Flask
from flask_restful import Api

from app_code.resource.joke_resources import SearchJoke, SaveJoke, UpdateJoke, DeleteJoke, AllJoke, FindJoke
from app_code.resource.math_resources import Math


os.environ["mariadb"] = json.dumps({'host': 'mysqldb','port': 3306,'user': 'root','password': 'Jvdf76sFWGYZHWUD','database': 'squadmarker'})

server = Flask(__name__)

api = Api(server)

@server.route('/')
def index():
    return 'Index Page test'

#-----------Joke Module-----------------

api.add_resource(SearchJoke, '/joke')
api.add_resource(SaveJoke, '/joke/save')
api.add_resource(UpdateJoke, '/joke/update')
api.add_resource(DeleteJoke, '/joke/delete')
api.add_resource(AllJoke, '/joke/all')
api.add_resource(FindJoke, '/joke/find')

#----------Math Module------------------
api.add_resource(Math, '/math')

if __name__ == "__main__":
   server.run(host='0.0.0.0', debug= True) 
