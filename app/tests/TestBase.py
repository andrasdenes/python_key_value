from collections import namedtuple

class TestBase:
    Form = namedtuple("form", ["key", "value", "get"])
    Request = namedtuple("Request", ["method", "form"])