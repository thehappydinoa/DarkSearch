class Dork(object):
    def __init__(self, *args, **kwargs):
        self.query = " ".join(args).strip()

        dorks = {
            "url": kwargs.get("url"),
            "title": kwargs.get("title"),
            "html_content": kwargs.get("html_content")
        }

        self.dorks = dorks

    def __str__(self):
        return "{0} {1}".format(str(self.query), self.parse_dorks(self.dorks)).strip()

    def combine_dorks(self, other):
        new_dorks = dict()
        for dorks in [self.dorks, other.dorks]:
            new_dorks.update((k, v)
                             for k, v in dorks.items() if v is not None)
        return new_dorks

    def AND(self, other):
        dorks = self.parse_dorks(self.combine_dorks(other))
        return self.parse_condition(self.query, "AND", other.query, dorks)

    def OR(self, other):
        dorks = self.parse_dorks(self.combine_dorks(other))
        return self.parse_condition(self.query, "OR", other.query, dorks)

    def NOT(self, other):
        dorks = self.parse_dorks(self.combine_dorks(other))
        return self.parse_condition(self.query, "NOT", other.query, dorks)

    @staticmethod
    def parse_condition(query_1, condition, query_2, dorks):
        return "\"{0}\" {1} \"{2}\" {3}".format(query_1, condition, query_2, dorks)

    @staticmethod
    def parse_dorks(dorks):
        dork_strings = list()
        for key, value in dorks.items():
            if value:
                dork_strings.append("{0}:\"{1}\"".format(key, str(value)))
        return " ".join(dork_strings)
