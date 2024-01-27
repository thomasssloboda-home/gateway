from app.router import router
from fastapi import FastAPI


class Server:
    app = None

    def initialize(self):
        self.app = FastAPI(
            version="0.0.1",
            title="Home Gateway",
            description="Exposes registered applications and their endpoints",
        )
        self.app.include_router(router)
        return self.app


instance = Server()
