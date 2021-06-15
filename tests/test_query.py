from darksearch import Query


def test_parse_queries():  # noqa: D103
    query = Query("query")
    assert str(query) == "query"

    query = Query("query", exact=True)
    assert str(query) == '"query"'


def test_and_queries():  # noqa: D103
    query = Query("query").and_("query")
    assert str(query) == "query AND query"

    query = Query("query", exact=True).and_("query", exact=True)
    assert str(query) == '"query" AND "query"'

    query = Query("query").and_("query", exact=True)
    assert str(query) == 'query AND "query"'


def test_or_queries():  # noqa: D103
    query = Query("query").or_("query")
    assert str(query) == "query OR query"

    query = Query("query", exact=True).or_("query", exact=True)
    assert str(query) == '"query" OR "query"'

    query = Query("query").or_("query", exact=True)
    assert str(query) == 'query OR "query"'


def test_not_queries():  # noqa: D103
    query = Query("query").not_("query")
    assert str(query) == "query NOT query"

    query = Query("query", exact=True).not_("query", exact=True)
    assert str(query) == '"query" NOT "query"'

    query = Query("query").not_("query", exact=True)
    assert str(query) == 'query NOT "query"'
