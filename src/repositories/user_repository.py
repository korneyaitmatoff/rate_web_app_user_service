from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.repositories.repository import Repository


class UserRepository(Repository):
    table: Type[DeclarativeMeta]

    def __init__(self, table: Type[DeclarativeMeta], database_handler):
        """Инит экземпляра класса и его родителя

        Args:
            table: объект таблицы сущности
        """
        super().__init__(table=table, database_handler=database_handler)
