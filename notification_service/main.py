from fastapi import FastAPI

from notification_service.server.server import Server

if __name__ == "__main__":
    app = FastAPI()
    server = Server(app)
    server.serve()
