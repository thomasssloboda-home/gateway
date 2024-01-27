from typing import Annotated

from app.database import instance as database
from app.types import Application, ApplicationResponse, CreateApplicationDTO
from fastapi import APIRouter, Body

router = APIRouter()


@router.get(
    "/",
    tags=["Applications"],
    name="Get applications",
    description="Retrieve registered applications",
    response_model=ApplicationResponse,
)
def get_applications_list():
    return {"apps": database.retrieve_applications_list_from_db()}


@router.post(
    "/",
    tags=["Applications"],
    name="Register an application",
    description="Register an application",
    response_model=Application,
)
def register_application(
    application: Annotated[CreateApplicationDTO, Body(embed=False)]
):
    return database.create_application_in_db(application)
