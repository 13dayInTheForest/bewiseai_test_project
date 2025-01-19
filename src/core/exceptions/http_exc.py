from fastapi import HTTPException, status


class AbstractHTTPException(HTTPException):
    _status_code = None
    _detail = None

    def __init__(self, detail: str | None = None):
        detail = detail or self._detail
        super().__init__(
            status_code=self._status_code,
            detail=detail,
        )


class NotFoundException(AbstractHTTPException):
    _detail = "Object not found."
    _status_code = status.HTTP_404_NOT_FOUND


class BadRequestException(AbstractHTTPException):
    _detail = "Failure! The creation request could not be processed."
    _status_code = status.HTTP_400_BAD_REQUEST


class CharacterLimitExceededException(AbstractHTTPException):
    _status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    _detail = "Exceeds the character limit"

    def __init__(self, field_name: str, max_length: int):
        detail = f"{field_name} exceeds the limit of {max_length} characters."
        super().__init__(detail=detail)
