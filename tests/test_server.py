from src.http_parser import parse_http_request


def test_simple_get2():
    raw = b"GET /test HTTP/1.1\r\nHost: localhost\r\n\r\n"
    parsed = parse_http_request(raw)

    assert parsed["method"] == "GET"
    assert parsed["path"] == "/test"
    assert parsed["version"] == "HTTP/1.1"
    assert parsed["headers"]["Host"] == "localhost"
    assert parsed["body"] == ""

