from src.backend.application.shared.errors import ApplicationError, NotFoundError


class FunnelError(ApplicationError):
    pass

class FunnelNotFoundError(NotFoundError, FunnelError):
    pass
