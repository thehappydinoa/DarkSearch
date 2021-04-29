import pytest
from darksearch import Client
from darksearch.exceptions import DarkSearchJSONDecodeException

client = Client(timeout=10)


def test_json_decode():  # noqa: D103
    with pytest.raises(DarkSearchJSONDecodeException):
        client.api_request("/")
