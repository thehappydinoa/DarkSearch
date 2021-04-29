import datetime
from unittest import TestCase

from pytest_httpserver import HTTPServer

from darksearch import Client


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

    server.expect_request("/api/crawling_status").respond_with_data(str(1_090_214))


class TestApi(TestCase):
    port = 4000
    base_url = f"http://localhost:{port}"

    def setUp(self):
        super().setUp()
        self.httpserver = HTTPServer("127.0.0.1", self.port)
        _setup_all(self.httpserver)
        self.httpserver.start()
        self.addCleanup(self.httpserver.stop)

        self.client = Client(base_url=self.base_url, timeout=10)

    def test_search_page_1(self):
        response = self.client.search("query")
        assert isinstance(response, dict)
        assert response.get("current_page") == 1

    def test_search_page_2(self):
        response = self.client.search("query", page=2)
        assert isinstance(response, dict)
        assert response.get("current_page") == 2

    def test_search_2_pages(self):
        response = self.client.search("query", pages=2)
        assert isinstance(response, list)
        assert len(response) == 2
        response_1, response_2 = response
        assert isinstance(response_1, dict)
        assert response_1.get("current_page") == 1
        assert isinstance(response_2, dict)
        assert response_2.get("current_page") == 2

    def test_search_2_pages_wait(self):
        wait_time = 5
        start = datetime.datetime.now()
        response = self.client.search("query", pages=2, wait=wait_time)
        end = datetime.datetime.now()
        elapsed = end - start
        assert isinstance(response, list)
        assert len(response) == 2
        response_1, response_2 = response
        assert isinstance(response_1, dict)
        assert response_1.get("current_page") == 1
        assert isinstance(response_2, dict)
        assert response_2.get("current_page") == 2
        assert elapsed.seconds >= wait_time

    def test_search_last_page(self):
        response = self.client.search(
            "super_specific_search_page_no_one_will_create_1234", pages=5
        )
        assert isinstance(response, list)
        assert len(response) == 1

    def test_crawling_status(self):
        response = self.client.crawling_status()
        assert isinstance(response, int)
