from typing import Dict, Tuple

def parse_http_request(raw_data: bytes)->Dict:
    """
    Парсит HTTP-запрос в виде сырых байтов.
    Возвращает словарь со структурой-

    {
        "method": "GET",
        "path": "/abc",
        "version": "HTTP/1.1",
        "headers": { ... },
        "body": ""
    }
    """

    try:
        text=raw_data.decode("utf-8", errors="replace")
    except Exception:
        text=str(raw_data)
    if "\r\n\r\n" in text:
        head, body=text.split("\r\n\r\n",1)
    else:
        head=text
        body=""
    lines=head.split("\r\n")
    if len(lines)<1:
        raise ValueError("Invalid HTTP request: no start str")
    start_line = lines[0].split(" ")
    if len(start_line)!=3:
        raise ValueError(f"Invalid start str:{lines[0]}")
    method,path,version=start_line
    headers={}
    for line in lines[1:]:
        if ":" not in line:
            continue
        key, value=line.split(":", 1)
        headers[key.strip()]=value.strip()
    return {
        "method": method,
        "path": path,
        "version": version,
        "headers": headers,
        "body": body,
    }
