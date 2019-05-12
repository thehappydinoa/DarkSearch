class DarkSearchException(Exception):
    pass

class DarkSearchPageNotFound(DarkSearchException):
    pass

class DarkSearchQuotaExceed(DarkSearchException):
    pass


class DarkSearchRequestException(DarkSearchException):
    pass


class DarkSearchJSONDecodeException(DarkSearchException):
    pass
