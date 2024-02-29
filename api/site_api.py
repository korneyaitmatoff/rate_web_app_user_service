from api.api import Api
from config import API_HOST, API_SITE_PORT


class SiteApi(Api):
    PATH = '/site'

    def __init__(self):
        super().__init__(host=API_HOST, port=API_SITE_PORT, path=self.PATH)

    def get_sites_by_user_id(self, user_id: int):
        """Получение списка сайтов по id юзера

        Args:
            id: идентификатор юзера
        """
        return self.get(url=f"{self.url}/user/{user_id}").json()
