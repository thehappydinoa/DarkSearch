import pytest
from darksearch import Client
from darksearch.exceptions import (DarkSearchJSONDecodeException,
                                   DarkSearchPageNotFound)

client = Client()


def test_page_not_found():
    with pytest.raises(DarkSearchPageNotFound):
        client.api_request("/not_a_real_path")


def test_json_decode():
    with pytest.raises(DarkSearchJSONDecodeException):
        client.api_request("/")
