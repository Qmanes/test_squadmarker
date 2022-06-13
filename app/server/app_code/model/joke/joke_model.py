from app_code.model.basic_model import Basic
from app_code.exception.basic_exception import RequiredException

class Joke(Basic):

    def __init__(self, uid = None, joke_new = None, joke_old = None, created_at = None, updated_at = None, deleted_at = None):

        self.joke_new = joke_new.lstrip() if joke_new else None
        self.joke_old = joke_old

        super().__init__(uid, created_at, updated_at, deleted_at)

    def field_update(self):

        return ["joke_new", "joke_old", "updated_at"]

    def save(self):

        self.assert_joke_valid(self.joke_new)

        super().save()

    def update(self, joke_new):

        super().update(joke_new)

        self.assert_joke_valid(joke_new)
    
    def assert_joke_valid(self, joke):

        if not joke:

            raise RequiredException("Joke")
    
