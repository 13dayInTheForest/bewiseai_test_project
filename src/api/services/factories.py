from fastapi import Depends

from src.core.factories.brokers import get_message_broker
from src.core.interfaces.applications import IApplicationsRepo
from src.core.interfaces.broker import IMessageBroker
from src.core.factories.repositories import get_applications_repo
from src.api.services.applications import ApplicationsService


async def get_applications_service(
        repo: IApplicationsRepo = Depends(get_applications_repo),
        broker: IMessageBroker = Depends(get_message_broker)
    ):
    return ApplicationsService(repo, broker)
