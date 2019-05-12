import json

import requests

from .exceptions import *


def api_request(path, base_url="https://darksearch.io", timeout=10, params=None):
    try:
        if params:
            response = requests.get(base_url + path, timeout=timeout, params=params)
        else:
            response = requests.get(base_url + path, timeout=timeout)
        if response.status_code == 404:
            raise DarkSearchPageNotFound
        elif response.status_code == 429:
            raise DarkSearchQuotaExceed
        return response.json()
    except requests.exceptions.RequestException:
        raise DarkSearchRequestException
    except json.decoder.JSONDecodeError as error:
        raise DarkSearchJSONDecodeException


def search(query, page=1):
    return api_request("/api/search", params={"query": query, "page": page})
