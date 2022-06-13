from app_code.model.basic_model import Basic
from ast import literal_eval
from itertools import chain
from collections import defaultdict
from app_code.exception.basic_exception import NotFoundException, LiteralFormatException

class Number(Basic):

    def __init__(self, uid = None, list_numbers = [], number = 0, created_at = None, updated_at = None, deleted_at = None):

        self.__set_list_numbers(list_numbers)

        self.__set_number(number)

        super().__init__(uid, created_at, updated_at, deleted_at)

    def get_sum(self, number = 1):

        result = self.__number  + number

        return result

    def get_lowest_common_multiple(self):

        numbers_decompose = [self.__get_numbers_decompose(number) for number in self.__list_numbers]

        lowest_common_multiple = self.__calculate_lowest_common_multiple(numbers_decompose)

        return lowest_common_multiple

    def __conver_to_list(self, list_numbers):

        literal_list_numbers = self.__get_literal_eval(list_numbers)
        
        return list(map(lambda number: int(str(number)), literal_list_numbers))

    def __get_literal_eval(self, list_numbers):

        try:
            
            return literal_eval(list_numbers)

        except Exception as error:
            
            raise LiteralFormatException(list_numbers)

    def __set_list_numbers(self, list_number):

        self.__list_numbers = self.__conver_to_list(list_number) if list_number else []

    def __set_number(self, number):

        self.__number = int(number)

    def __calculate_lowest_common_multiple(self, numbers_decompose):

        numbers_decompose_union = self.__get_numbers_decompose_union(numbers_decompose)

        lowest_common_multiple = 1
        
        for key, number_decompose_union in numbers_decompose_union.items():
            
            base = int(key)

            exponential = max(numbers_decompose_union[key])

            lowest_common_multiple *= pow(base, exponential)

        return lowest_common_multiple

    def __get_numbers_decompose(self, number):
        
        aux = number

        control_divisor = 2

        numbers_decompose = {}

        while control_divisor < number or (not numbers_decompose and control_divisor == number):

            if  aux % control_divisor == 0:

                aux = aux / control_divisor
                
                numbers_decompose.update({control_divisor: numbers_decompose.get(control_divisor, 0) + 1})

                control_divisor = 2

            else:
                
                control_divisor += 1

        return numbers_decompose


    def __get_numbers_decompose_union(self, numbers_decompose):
        
        numbers_decompose_union = defaultdict(list)

        for key, number_decompose_union in chain(*[number_decompose.items() for number_decompose in numbers_decompose]):
            
            numbers_decompose_union[key].append(number_decompose_union)

        return numbers_decompose_union
