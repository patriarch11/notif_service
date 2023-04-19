from dataclasses import dataclass

from fastapi import FastAPI, APIRouter

__all__ = ["Routes"]


@dataclass(frozen=True)
class Routes:
    routers: tuple[APIRouter, ...]

    def register_routes(self, app: FastAPI):
        for router in self.routers:
            app.include_router(router)
