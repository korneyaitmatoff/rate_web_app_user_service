from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class DatabaseHandler:
    """Класс для работы с базой данных"""

    def __init__(self):
        self.url = f"postgresql://tavern:tavern@45.9.43.40:5432/app"
        self.engine = create_engine(url=self.url)
        self.session = None

    def __enter__(self):
        """Контекстный менеджер, создание сессии"""

        self.create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Контекстный менеджер, закрытие сессии"""

        if exc_type:
            raise Exception(
                f'Произошла ошибка во время работы с БД!\n'
                f'\tТип:      {exc_type}\n'
                f'\tЗначение: {exc_val}\n'
                f'\tСтек:     {exc_tb}'
            )

        self.close_session()

    def create_session(self):
        """Создание сессии"""

        self.session = sessionmaker(bind=self.engine)()

    def close_session(self):
        """Закрытие сессии"""

        self.session.close()

    def test_connection(self):
        """Проверка соединения с бд"""

        self.create_session()
        self.session.execute(text("SELECT 1;"))
        self.close_session()

    def select(self, table, filters: tuple, limit: int = 1000, offset: int = None) -> list:
        """Получение данных из таблицы"""

        query = self.session.query(table).filter(*filters).limit(limit)

        if offset:
            query = query.offset(offset)

        return query.all()

    def insert(self, table, data: dict):
        """Добавление записи"""

        self.session.add(record := table(**data))
        self.session.commit()
        self.session.refresh(record)

        return record

    def delete(self, table, filters: tuple):
        """Удаление записи"""

        self.session.query(table).filter(*filters).delete()
        self.session.commit()

    def update(self, table, filters: tuple, data: dict):
        self.session.query(table).filter(*filters).update(data)
        self.session.commit()
