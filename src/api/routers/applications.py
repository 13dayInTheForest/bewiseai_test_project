from fastapi import APIRouter, Depends

from src.api.interfaces.applications import IApplicationsService
from src.api.services.factories import get_applications_service
from src.core.schemas.applications import (
    CreateApplicationSchema,
    ApplicationSchema,
    ApplicationsPageSchema
)


router = APIRouter(
    prefix='/applications'
)


@router.post('/', response_model=ApplicationSchema)
async def create_application(application: CreateApplicationSchema,
                             service: IApplicationsService = Depends(get_applications_service)):
    return await service.create_application(application)


@router.get('/', response_model=ApplicationsPageSchema)
async def get_page(username: str = None, page: int = 1, size: int = 20,
                   service: IApplicationsService = Depends(get_applications_service)):
    return await service.get_page(username, page, size)
