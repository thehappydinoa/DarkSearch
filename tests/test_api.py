from darksearch import crawling_status, search


def test_search_page_1():
    response = search("query")
    assert isinstance(response, dict)
    assert response.get("current_page") == 1


def test_search_page_2():
    response = search("query", page=2)
    assert isinstance(response, dict)
    assert response.get("current_page") == 2


def test_search_2_pages():
    response = search("query", pages=2)
    assert isinstance(response, list)
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2


def test_search_2_pages_wait():
    response = search("query", pages=2, wait=2)
    assert isinstance(response, list)
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2


def test_crawling_status():
    response = int(crawling_status())
    assert isinstance(response, int)
