from src.handler import handle_request

def test_handler_basic():
    parsed={
        "method": "GET",
        "path": "/hello",
        "version": "HTTP/1.1",
        "headers": {"Host": "localhost"},
        "body": ""}
    response=handle_request(parsed)
    assert "Method:GET" in response
    assert "Path:/hello" in response
    assert "Headers:{'Host': 'localhost'}" in response
def test_handler_post():
    parsed={
        "method": "POST",
        "path": "/submit",
        "version": "HTTP/1.1",
        "headers": {},
        "body": "data=123"}

    response=handle_request(parsed)
    assert "data=123" in response
