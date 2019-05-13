import pytest
from darksearch import api_request
from darksearch.exceptions import (DarkSearchJSONDecodeException,
                                   DarkSearchPageNotFound)


def test_page_not_found():
    with pytest.raises(DarkSearchPageNotFound):
        api_request("/not_a_real_path")


def test_json_decode():
    with pytest.raises(DarkSearchJSONDecodeException):
        api_request("/")
