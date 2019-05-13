from darksearch import Dork


def test_parse_dorks():
    dork = Dork("query")
    assert str(dork) == "query"

    dork = Dork("query", url="*.onion*")
    assert str(dork) == "query url:\"*.onion*\""

    dork = Dork("query", title="Title")
    assert str(dork) == "query title:\"Title\""

    dork = Dork("query", html_content="<h1>Header</h1>")
    assert str(dork) == "query html_content:\"<h1>Header</h1>\""


def test_and_dorks():
    dork_1 = Dork("query", url="*.onion*")
    dork_2 = Dork("query")
    dork = dork_1.AND(dork_2)
    assert str(dork) == "\"query\" AND \"query\" url:\"*.onion*\""

    dork_1 = Dork("query", title="Title")
    dork_2 = Dork("query")
    dork = dork_1.AND(dork_2)
    assert str(dork) == "\"query\" AND \"query\" title:\"Title\""

    dork_1 = Dork("query", html_content="<h1>Header</h1>")
    dork_2 = Dork("query")
    dork = dork_1.AND(dork_2)
    assert str(dork) == "\"query\" AND \"query\" html_content:\"<h1>Header</h1>\""

    dork_1 = Dork("query")
    dork_2 = Dork("query", url="*.onion*")
    dork = dork_1.AND(dork_2)
    assert str(dork) == "\"query\" AND \"query\" url:\"*.onion*\""

    dork_1 = Dork("query")
    dork_2 = Dork("query", title="Title")
    dork = dork_2.AND(dork_1)
    assert str(dork) == "\"query\" AND \"query\" title:\"Title\""


def test_or_dorks():
    dork_1 = Dork("query", url="*.onion*")
    dork_2 = Dork("query")
    dork = dork_1.OR(dork_2)
    assert str(dork) == "\"query\" OR \"query\" url:\"*.onion*\""

    dork_1 = Dork("query", title="Title")
    dork_2 = Dork("query")
    dork = dork_1.OR(dork_2)
    assert str(dork) == "\"query\" OR \"query\" title:\"Title\""

    dork_1 = Dork("query", html_content="<h1>Header</h1>")
    dork_2 = Dork("query")
    dork = dork_1.OR(dork_2)
    assert str(dork) == "\"query\" OR \"query\" html_content:\"<h1>Header</h1>\""


def test_not_dorks():
    dork_1 = Dork("query", url="*.onion*")
    dork_2 = Dork("query")
    dork = dork_1.NOT(dork_2)
    assert str(dork) == "\"query\" NOT \"query\" url:\"*.onion*\""

    dork_1 = Dork("query", title="Title")
    dork_2 = Dork("query")
    dork = dork_1.NOT(dork_2)
    assert str(dork) == "\"query\" NOT \"query\" title:\"Title\""

    dork_1 = Dork("query", html_content="<h1>Header</h1>")
    dork_2 = Dork("query")
    dork = dork_1.NOT(dork_2)
    assert str(dork) == "\"query\" NOT \"query\" html_content:\"<h1>Header</h1>\""
