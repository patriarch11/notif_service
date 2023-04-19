import uvicorn
from fastapi import FastAPI

from notification_service.server.routes import __routes__
from notification_service.settings import __settings__


class Server:
    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)

    def serve(self):
        uvicorn.run(self.__app, host=__settings__.host, port=__settings__.port)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_routes(app: FastAPI):
        __routes__.register_routes(app)

    @staticmethod
    def __register_events(app: FastAPI):
        ...
