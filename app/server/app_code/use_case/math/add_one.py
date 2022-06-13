from app_code.model.math.number import Number

def handler(number_base):
    
    number = Number(number = number_base)
    
    result = number.get_sum()

    return "the sum {number_base} + 1 is : {result}".format(number_base = number_base, result = result)
