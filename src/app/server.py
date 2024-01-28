from app.router import router
from app._version import __version__
from fastapi import FastAPI


class Server:
    app = None

    def initialize(self):
        self.app = FastAPI(
            version=__version__,
            title="Home Gateway",
            description="Exposes registered applications and their endpoints",
        )
        self.app.include_router(router)
        return self.app


instance = Server()
