from typing import Dict, Any
from logger import logger


def handle_request(parsed: Dict[str, Any]) -> str:
    """
    Обрабатывает распаршенный HTTP-запрос и формирует тело ответа
    parsed:dict[str, Any]

    Args:
        args: parsed:{
            "method":str,
            "path":str,
            "version":str,
            "headers":Dict[str, str],
            "body":str
        }

    Returns:
        str: текстовый ответ который будет отправлен клиенту
    """
    method=parsed.get("method", "?")
    path=parsed.get("path", "?")
    headers=parsed.get("headers", {})
    body=parsed.get("body", "")

    logger.debug("=== Parsed Request ===")
    logger.debug(f"Method : {method}")
    logger.debug(f"Path   : {path}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Body   : {body}")
    logger.debug("======================")
    response_text=(
        "Request processed by handler.\n"
        f"Method:{method}\n"
        f"Path:{path}\n"
        f"Headers:{headers}\n"
        f"Body:{body}\n"
    )
    logger.info("Request successfully handled")
    return response_text
