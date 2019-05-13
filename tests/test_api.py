from darksearch import Client

client = Client()


def test_search_page_1():
    response = client.search("query")
    assert isinstance(response, dict)
    assert response.get("current_page") == 1


def test_search_page_2():
    response = client.search("query", page=2)
    assert isinstance(response, dict)
    assert response.get("current_page") == 2


def test_search_2_pages():
    response = client.search("query", pages=2)
    assert isinstance(response, list)
    assert len(response) == 2
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2


def test_search_2_pages_wait():
    response = client.search("query", pages=2, wait=2)
    assert isinstance(response, list)
    assert len(response) == 2
    response_1, response_2 = response
    assert isinstance(response_1, dict)
    assert response_1.get("current_page") == 1
    assert isinstance(response_2, dict)
    assert response_2.get("current_page") == 2


def test_search_last_page():
    response = client.search(
        "super_specific_search_page_no_one_will_create", pages=5)
    assert isinstance(response, list)
    assert len(response) == 1

# DEBUG: Hitting me with a 504 Gateway Time-out
# def test_crawling_status():
#     response = client.crawling_status()
#     assert isinstance(response, int)
