import socket 
from logger import logger
import threading
from .http_parser import parse_http_request


HOST="0.0.0.0"
PORT=8080
running=True

def input_watcher()->None:
    """Слушает ввод в консоль чтобы можно было остановить сервер"""
    global running
    while True:
        cmd=input()
        if cmd.strip()=="exit":
            logger.info("Server stopped")
            running=False
            break 


def server_start():
    """Запуск TCP сервера"""
    global running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST,PORT))
        server_socket.listen()
        server_socket.settimeout(1)
        logger.info(f"Server started:{HOST}:{PORT}")
        while running:
            try:
                conn,addr=server_socket.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            logger.info(f"Client connected on {addr}")
            with conn:
                try:
                    raw_request=conn.recv(4096)
                except ConnectionResetError:
                    logger.warning("Client closed the connection")
                    continue
                if not raw_request:
                    logger.warning("Empty request")
                    continue
                logger.debug("\n===== RAW REQUEST =====")
                logger.debug(raw_request.decode(errors="replace"))
                logger.debug("========================\n")
                response_body="Request received"
                response=("HTTP/1.1 200 OK\r\n"
                        f"Content-Length: {len(response_body)}\r\n"
                            "Content-Type: text/plain\r\n"
                            "Connection: close\r\n"
                            "\r\n"
                            f"{response_body}"
                        )
                conn.sendall(response.encode())
                logger.info(f"Client connected:{addr}")

    logger.info("Server stopped")
if __name__=="__main__":
    watcher = threading.Thread(target=input_watcher, daemon=True)
    watcher.start()
    server_start()