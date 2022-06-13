from  uuid import uuid1
from datetime import datetime
class Basic():

    def __init__(self, uid = None, created_at = None, updated_at = None, deleted_at = None):

        self.uid = uid or str(uuid1())
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def as_dict(self):

        #refector
        self.created_at = self.__datetime_to_str(self.created_at)
        self.updated_at = self.__datetime_to_str(self.updated_at) if self.updated_at else self.updated_at
        self.deleted_at = self.__datetime_to_str(self.deleted_at) if self.deleted_at else self.deleted_at

        return self.__dict__

    def save(self):

        self.created_at = self.__get_now()

    def delete(self):

        self.deleted_at = self.__get_now()

    def update(self, joke_new):

        self.updated_at = self.__get_now()

        self.joke_old = self.joke_new
        
        self.joke_new = joke_new
    
    def get_tuple_fields(self):

        obj_dict = self.as_dict()

        return tuple(obj_dict.keys())

    def get_tuple_values(self):

        obj_dict = self.as_dict()

        return tuple(obj_dict.values())

    def __get_now(self):

        return datetime.now()

    def get_uid(self):

        return self.uid

    def __datetime_to_str(self, datetime_value):

        return datetime_value.strftime("%Y/%m/%d, %H:%M:%S") if isinstance(datetime_value, datetime) else datetime_value