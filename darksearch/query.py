from typing import List


class Query:
    def __init__(self, query: str, exact: bool = False):
        self._query_list: List[str] = []
        self.add_query(query, exact=exact)

    def __str__(self):
        return " ".join(self._query_list)

    def add_query(self, string: str, exact: bool = False):
        if exact:
            string = '"' + string + '"'
        self._query_list.append(string)
        return self

    def and_(self, query: str, exact: bool = False):
        self.add_query("AND")
        return self.add_query(query.strip(), exact=exact)

    def or_(self, query: str, exact: bool = False):
        self.add_query("OR")
        return self.add_query(query.strip(), exact=exact)

    def not_(self, query: str, exact: bool = False):
        self.add_query("NOT")
        return self.add_query(query.strip(), exact=exact)
