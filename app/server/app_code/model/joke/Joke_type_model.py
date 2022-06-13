from app_code.model.basic_model import Basic

class JokeType(Basic):

    def __init__(self, uid = None, name = None, endpoint = None, param = None, status = None, created_at = None, updated_at = None, deleted_at):

        self.name = name
        self.endpoint = endpoint
        self.param = param
        self.status = status

        super().__init__(uid, created_at, updated_at, deleted_at)
