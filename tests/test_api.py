import datetime

import pytest
from pytest_httpserver import HTTPServer

from darksearch import Client

PORT = 4000


def _setup_all(server: HTTPServer):
    server.expect_request(
        "/api/search", query_string="query=query&page=1"
    ).respond_with_json({"current_page": 1, "last_page": 5})

    server.expect_request(
        "/api/search", query_string="query=query&page=2"
    ).respond_with_json({"current_page": 2, "last_page": 5})

    server.expect_request(
        "/api/search",
        query_string="query=super_specific_search_page_no_one_will_create_1234&page=1",
    ).respond_with_json({"current_page": 1, "last_page": 0})

    server.expect_request("/api/crawling_status").respond_with_data(str(1090214))


@pytest.fixture
def httpserver_listen_address():
    return ("127.0.0.1", PORT)


@pytest.fixture
def darksearch_client():
    base_url = f"http://localhost:{PORT}"
    return Client(base_url=base_url, timeout=10)


def test_search_page_1(httpserver: HTTPServer, darksearch_client: Client):  # noqa: D103
    _setup_all(httpserver)
    response = darksearch_client.search("query")
    assert isinstance(response, dict)
    assert response.get("current_page") == 1


def test_search_page_2(httpserver: HTTPServer, darksearch_client: Client):  # noqa: D103
    _setup_all(httpserver)
    response = darksearch_client.search("query", page=2)
    assert isinstance(response, dict)
    assert response.get("current_page") == 2


def test_search_2_pages(
    httpserver: HTTPServer, darksearch_client: Client
):  # noqa: D103
    _setup_all(httpserver)
    response = darksearch_client.search("query", pages=2)
    assert isinstance(response, list)
    assert len(response) == 2
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2


def test_search_2_pages_wait(
    httpserver: HTTPServer, darksearch_client: Client
):  # noqa: D103
    _setup_all(httpserver)
    start = datetime.datetime.now()
    response = darksearch_client.search("query", pages=2, wait=10)
    end = datetime.datetime.now()
    elapsed = end - start
    assert isinstance(response, list)
    assert len(response) == 2
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2
    assert elapsed.seconds >= 10


def test_search_last_page(
    httpserver: HTTPServer, darksearch_client: Client
):  # noqa: D103
    _setup_all(httpserver)
    response = darksearch_client.search(
        "super_specific_search_page_no_one_will_create_1234", pages=5
    )
    assert isinstance(response, list)
    assert len(response) == 1


def test_crawling_status(
    httpserver: HTTPServer, darksearch_client: Client
):  # noqa: D103
    _setup_all(httpserver)
    response = darksearch_client.crawling_status()
    assert isinstance(response, int)
