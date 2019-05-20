import datetime

from darksearch import Client

client = Client(timeout=10)


def test_search_page_1():  # noqa: D103
    response = client.search("query")
    assert isinstance(response, dict)
    assert response.get("current_page") == 1


def test_search_page_2():  # noqa: D103
    response = client.search("query", page=2)
    assert isinstance(response, dict)
    assert response.get("current_page") == 2


def test_search_2_pages():  # noqa: D103
    response = client.search("query", pages=2)
    assert isinstance(response, list)
    assert len(response) == 2
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2


def test_search_2_pages_wait():  # noqa: D103
    start = datetime.datetime.now()
    response = client.search("query", pages=2, wait=2)
    end = datetime.datetime.now()
    elapsed = end - start
    assert isinstance(response, list)
    assert len(response) == 2
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2
    assert elapsed.seconds >= 1


def test_search_last_page():  # noqa: D103
    response = client.search(
        "super_specific_search_page_no_one_will_create", pages=5
    )
    assert isinstance(response, list)
    assert len(response) == 1


def test_crawling_status():  # noqa: D103
    response = client.crawling_status()
    assert isinstance(response, int)
