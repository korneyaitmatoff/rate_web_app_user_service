from src.services.service import Service
from src.repositories.repository import Repository
from src.schemas.user import User, AuthUser, UserInput


class UserService(Service):
    """Класс-сервис для работы с сущностью "Пользователь" """

    def __init__(self, repository: Repository):
        super().__init__(repository=repository)

    def get_users(self):
        return self.read()

    def get_user_by_id(self, user_id: int) -> User:
        return self.read(filters=(self.repository.table.id == user_id,))[0]

    def edit_user(self, user_id: int, user: User):
        self.repository.update(id=user_id, data=dict(user))
        return user

    def create_user(self, user: UserInput):
        return self.create(dict(user))

    def delete_user(self, user_id: int):
        self.delete(filters=(self.repository.table.id == user_id,))

    def auth(self, user: AuthUser):
        data = self.read(
            filters=(
                self.repository.table.login == user.login,
                self.repository.table.password == user.password,
            )
        )
        return data[0].id if data else -1
