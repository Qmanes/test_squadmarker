import pytest
from app_code.model.math.number import Number
from app_code.model.joke.joke_model import Joke
from app_code.exception.basic_exception import NotFoundException, LiteralFormatException, UrlNotValidException, RequiredException
from app_code.service.utils.petition import get as get_petition
from app_code.use_case.joke.joke.search import get_joke_type

def test_get_sum_valid():

    number = Number(number = "400")

    assert number.get_sum() == 401

def test_get_lowest_common_multiple_valid():

    number = Number(list_numbers = "[7,354,24,9]")
    
    assert number.get_lowest_common_multiple() == 29736

def test_get_sum_type_float_error():

    with pytest.raises(ValueError):

        assert Number(number = "400.5")

def test_get_sum_type_str_error():

    with pytest.raises(ValueError):

        assert Number(number = "1234textramdon")

def test_get_lowest_common_multiple_literal_error():

    with pytest.raises(LiteralFormatException):

        assert Number(list_numbers = "[7,354,24,9]textramdon")

def test_get_lowest_common_multiple_type_float_error():

    with pytest.raises(ValueError):

        assert Number(list_numbers = "[7.3,354.5,24.7,9.9]")

def test_get_lowest_common_multiple_type_str_error():

    with pytest.raises(ValueError):

        assert Number(list_numbers = "['textramdon',354.5,24.7,'textramdon']")
