import time
import warnings

import requests

from .exceptions import *

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class Client(object):
    def __init__(self, base_url="https://darksearch.io", headers=None, proxies=None):
        self.base_url = base_url
        self.headers = headers
        self.proxies = proxies

    def api_request(self, path, params=None, json=True):
        """
        :param path: Path to be requested
        :param base_url: Base URL to be combined with the path
        :param params: Base URL to be combined with the path
        :type path: str
        :type base_url: str
        :type params: dict
        :return: JSON Response
        :rtype: dict
        """
        try:
            response = requests.get(
                self.base_url + path, params=params, headers=self.headers, proxies=self.proxies)
            if response.status_code == 404:
                raise DarkSearchPageNotFound
            if response.status_code == 429:
                raise DarkSearchQuotaExceed
            if json:
                return response.json()
            return response.content
        except requests.exceptions.RequestException:
            raise DarkSearchRequestException
        except JSONDecodeError:
            print(response.content)
            raise DarkSearchJSONDecodeException

    def api_search(self, query, page):
        """
        :param query: Query to be searched
        :param page: Page number of the search
        :type query: str
        :type page: int
        :return: search results
        :rtype: dict
        """
        if page < 1:
            page = 1
        return self.api_request("/api/search", params={"query": query, "page": page})

    def search(self, query, **kwargs):
        """
        :param query: Query to be searched
        :param page: Page number of the search
        :param pages: Pages to be returned
        :param wait: Time to wait between requests
        :type query: str
        :type page: int
        :type pages: int
        :type wait: int
        :return: search results
        :rtype: list or dict
        """
        page = kwargs.get("page")
        pages = kwargs.get("pages")
        wait = kwargs.get("wait")

        if pages and not page:
            results = list()
            try:
                for page_i in range(pages):
                    response = self.api_search(query, page_i + 1)
                    results.append(response)
                    if response.get("last_page") <= page_i + 1:
                        break
                    if wait:
                        time.sleep(wait)
            except DarkSearchQuotaExceed:
                warnings.warn(
                    "Seach Quota Exceeded, please keep searches to less than 30 per minute")
            return results
        if not page:
            page = 1
        return self.api_search(query, page)

    def crawling_status(self):
        """
        :return: crawling_status
        :rtype: int
        """
        return int(self.api_request("/api/crawling_status", json=False))
