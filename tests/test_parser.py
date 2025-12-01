from src.http_parser import parse_http_request
import pytest
def test_simple_get():
    raw=b"GET /test HTTP/1.1\r\nHost: localhost\r\n\r\n"
    parsed=parse_http_request(raw)
    assert parsed["method"]=="GET"
    assert parsed["path"]=="/test"
    assert parsed["version"]=="HTTP/1.1"
    assert parsed["headers"]["Host"]=="localhost"
    assert parsed["body"]==""
def test_get_with_body():
    raw=(
        b"POST /login HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"Content-Length: 11\r\n\r\n"
        b"hello=world")
    parsed=parse_http_request(raw)
    assert parsed["method"]=="POST"
    assert parsed["body"]=="hello=world"

def test_invalid_request_missing_start_line():
    raw=b"Host: localhost\r\n\r\n"
    with pytest.raises(ValueError):
        parse_http_request(raw)

def test_invalid_start_line_wrong_format():
    raw=b"GET /only_two_parts\r\nHost: localhost\r\n\r\n"
    with pytest.raises(ValueError):
        parse_http_request(raw)

def test_headers_parsing():
    raw=(
        b"GET / HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"User-Agent: test-client\r\n"
        b"Accept: */*\r\n\r\n")
    parsed=parse_http_request(raw)
    assert parsed["headers"]["User-Agent"]=="test-client"
    assert parsed["headers"]["Accept"]=="*/*"
