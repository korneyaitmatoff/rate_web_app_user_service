from pydantic import StrictInt
from requests import get, Response
from loguru import logger


class Api:
    """,,,"""

    def __init__(self, host, port, path='/'):
        self.url = f"{host}:{port}{path}"

    def get(self, url: StrictInt, data: dict = {}) -> Response:
        """Метод для отправки GET запроса

        Args:
            url: ссылка запроса
            data: данные запроса
        """
        logger.debug(f"Отправка запроса в: {url}. Данные запроса: {str(data)}")

        return get(url=url, data=data)
