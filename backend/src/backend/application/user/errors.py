from src.backend.application.shared.errors import ApplicationError


class UserError(ApplicationError):
    pass

class UserNotFoundError(UserError):
    pass