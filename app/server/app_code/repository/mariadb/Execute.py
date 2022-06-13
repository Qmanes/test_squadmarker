from app_code.repository.mariadb.query import execute_insert, execute_find_id, execute_all , execute_update, execute_delete, execute_find_one, execute_sql, execute_setup
from app_code.exception.basic_exception import NotFoundException
class Execute():

    def __init__(self, table = None, obj = None, title = None):

        self.table = table

        self.obj = obj

        self.title = title

    def find_or_fail(self, data_id):

        result = execute_find_id(table=self.table, value=data_id)

        if result:

            return self.obj(*result)
        
        raise NotFoundException(self.title)

    def all(self, condition = None):

        list_all = execute_all(self.table, condition = condition)

        return list(map(lambda obj: self.obj(*obj), list_all))

    def save(self, obj):

        fields = obj.get_tuple_fields()
        
        values = obj.get_tuple_values()

        value_length = str(tuple(['?' for value in fields]))

        value_length = value_length.replace("'","")
        
        execute_insert(self.table, fields, values, value_length)
        
        return self.find_or_fail(obj.get_uid())

    def update(self,obj, condition = None):

        condition = "uid = '{}'".format(obj.get_uid())

        field_update = obj.field_update()

        obj_dict = obj.as_dict()

        data = ""

        for key, field in enumerate(field_update):
            
            data += "{field} = '{value}'".format(field = field, value = obj_dict.get(field))

            if (key + 1) < len(field_update):

                data += ","

        execute_update(table=self.table, data = data, condition = condition)

        return self.find_or_fail(obj.get_uid())

    def delete(self, obj):

        condition = "uid = '{}'".format(obj.get_uid())

        execute_delete(table=self.table, condition = condition, deleted_at = obj.deleted_at)