import pytest
from app_code.model.math.number import Number
from app_code.model.joke.joke_model import Joke
from app_code.exception.basic_exception import NotFoundException, LiteralFormatException, UrlNotValidException, RequiredException
from app_code.service.utils.petition import get as get_petition
from app_code.use_case.joke.joke.search import get_joke_type


def test_send_petition_url_not_valid():

    with pytest.raises(UrlNotValidException):

        assert get_petition("test_ramdon")

def test_get_joke_type():

    with pytest.raises(NotFoundException):

        assert get_joke_type("test_ramdon")

def test_joke_save_required():

    joke = Joke(joke_new = "")

    with pytest.raises(RequiredException):

        assert joke.save()

def test_joke_update_required():

    joke = Joke(joke_new = "test_ramdon")

    with pytest.raises(RequiredException):

        assert joke.update("")

def test_joke_save_valid():

    joke = Joke(joke_new = "test_ramdon")

    joke.save()

def test_joke_update_valid():

    joke = Joke(joke_new = "test_ramdon")

    joke.update("test_ramdom_update")