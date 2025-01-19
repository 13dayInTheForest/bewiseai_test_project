from fastapi import Depends
from src.core.interfaces.applications import IApplicationsRepo
from src.core.repositories.factories import get_applications_repo
from src.api.services.applications import ApplicationsService


async def get_applications_service(repo: IApplicationsRepo = Depends(get_applications_repo)):
    return ApplicationsService(repo)
