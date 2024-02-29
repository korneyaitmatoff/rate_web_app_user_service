from api.api import Api
from config import API_HOST, API_COMMENT_PORT


class CommentApi(Api):
    PATH = '/comment'

    def __init__(self):
        super().__init__(host=API_HOST, port=API_COMMENT_PORT, path=self.PATH)

    def get_comments_by_user_id(self, user_id: int):
        """Получение списка комментариев по id юзера

        Args:
            id: идентификатор юзера
        """
        return self.get(url=f"{self.url}/list/{user_id}").json()
