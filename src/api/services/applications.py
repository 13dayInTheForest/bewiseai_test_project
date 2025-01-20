from src.core.exceptions.base_exc import MessageBrokerMessageNotSent
from src.core.interfaces.applications import IApplicationsRepo
from src.core.interfaces.broker import IMessageBroker
from src.core.schemas.applications import (
    ApplicationSchema,
    CreateApplicationSchema,
    ApplicationsPageSchema)
from src.core.exceptions import http_exc


class ApplicationsService:
    def __init__(self, repo: IApplicationsRepo, message_broker: IMessageBroker):
        self.repo = repo
        self.message_broker = message_broker

    async def create_application(self, application: CreateApplicationSchema) -> ApplicationSchema:
        if len(application.username) > 80:
            raise http_exc.CharacterLimitExceededException('Name', 80)
        if len(application.description) > 3000:
            raise http_exc.CharacterLimitExceededException('Description', 3000)

        app_id = await self.repo.create(application.dict())
        app = await self.repo.select_one_by_id(app_id)
        if app is None:
            await self.repo.rollback()
            raise http_exc.BadRequestException

        message_status = await self.message_broker.send_message(app)
        if not message_status:
            await self.repo.rollback()
            raise MessageBrokerMessageNotSent
        await self.repo.commit()
        return app

    async def get_page(self, username: str = None,
                       page: int = 1,
                       size: int = 20
                       ) -> ApplicationsPageSchema:
        if page < 1:  # чтобы при пагинации ничего не падало
            page = 1
        applications = await self.repo.select(username=username, page=page, size=size)
        return applications
