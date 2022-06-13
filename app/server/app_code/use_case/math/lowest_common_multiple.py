from app_code.model.math.number import Number

def handler(list_numbers):
    
    number = Number(list_numbers = list_numbers)

    lowest_common_multiple = number.get_lowest_common_multiple()

    return "greatest common multiple of {list_numbers} is :{lowest_common_multiple}".format(list_numbers = list_numbers, \
                lowest_common_multiple = lowest_common_multiple)