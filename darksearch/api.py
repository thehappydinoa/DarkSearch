from time import sleep
from warnings import warn
from typing import Iterable
from json.decoder import JSONDecodeError

import requests
from requests.compat import urljoin

from .exceptions import (
    DarkSearchJSONDecodeException,
    DarkSearchPageNotFound,
    DarkSearchQuotaExceed,
    DarkSearchRequestException,
    DarkSearchServerError,
)


def lookahead(iterable: Iterable):
    """Pass through all values from the given iterable, augmented by the
    information if there are more values to come after the current one
    (True), or if it is the last value (False).
    """
    it = iter(iterable)
    last = next(it)
    for val in it:
        yield last, True
        last = val
    yield last, False


class Client(object):
    """Client object for DarkSearch API."""

    def __init__(
        self,
        base_url: str = "https://darksearch.io",
        timeout: int = 30,
        headers: dict = {},
        proxies: dict = {},
    ):
        """Initialize this client with the given parameters.

        :param base_url: Base URL for the API
        :param timeout: Timeout for the requests
        :param headers: Headers for the request
        :param proxies: Proxies configuration
        :type base_url: str
        :type timeout: int
        :type headers: dict
        :type proxies: dict
        """
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers
        self.proxies = proxies

    def api_request(self, path: str, params: dict = {}, json: bool = True):
        """Perform an API request to DarkSearch.

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
                urljoin(self.base_url, path),
                timeout=self.timeout,
                params=params,
                headers=self.headers,
                proxies=self.proxies,
            )

            if response.status_code == 404:
                raise DarkSearchPageNotFound
            if response.status_code == 429:
                raise DarkSearchQuotaExceed
            if response.status_code == 504:
                raise DarkSearchServerError

            if json:
                return response.json()

            return response.content

        except requests.exceptions.RequestException:
            raise DarkSearchRequestException

        except JSONDecodeError:
            print(response.content)
            raise DarkSearchJSONDecodeException

    def api_search(self, query: str, page: int):
        """Perform low level search with the API.

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

    def search(self, query: str, **kwargs):
        """Perform search with the API.

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
                for page_i, has_more in lookahead(range(pages)):
                    response = self.api_search(query, page_i + 1)
                    results.append(response)
                    if response.get("last_page") <= page_i + 1:
                        break
                    if wait and has_more:
                        sleep(wait)
            except DarkSearchQuotaExceed:
                warn(
                    "Seach Quota Exceeded, please keep searches to less than "
                    "30 per minute"
                )
            return results
        if not page:
            page = 1
        return self.api_search(query, page)

    def crawling_status(self) -> int:
        """Return the number of indexed pages in DarkSearch.

        :return: crawling_status
        :rtype: int
        """
        return int(self.api_request("/api/crawling_status", json=False))
