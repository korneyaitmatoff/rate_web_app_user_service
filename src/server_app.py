from fastapi import FastAPI


class Server:

    def __init__(self):
        self.app = FastAPI()

    def register_routes(self, routes):
        for route in routes:
            route.register_routes(self.app)

    def register_db(self):
        ...
