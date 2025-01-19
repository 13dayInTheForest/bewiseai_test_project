import datetime
from pydantic import BaseModel


class ApplicationSchema(BaseModel):
    id: int
    username: str
    description: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class CreateApplicationSchema(BaseModel):
    username: str
    description: str


class ApplicationsPageSchema(BaseModel):
    result: list[ApplicationSchema]
    page: int
    size: int
