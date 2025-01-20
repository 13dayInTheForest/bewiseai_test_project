class AbstractBaseException(Exception):
    _message = None

    def __init__(self, message: str | None = None):
        super().__init__(message or self._message)


class ConnectFailedException(AbstractBaseException):
    _message = "Database Connect Failed"


class MessageBrokerNotImplement(AbstractBaseException):
    _message = "Message Broker not implemented"


class MessageBrokerMessageNotSent(AbstractBaseException):
    _message = "Message not sent"
