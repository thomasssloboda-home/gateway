from pydantic import BaseModel


class Application(BaseModel):
    id: int
    name: str
    url: str


class ApplicationResponse(BaseModel):
    apps: list[Application]


class CreateApplicationDTO(BaseModel):
    name: str
    url: str
