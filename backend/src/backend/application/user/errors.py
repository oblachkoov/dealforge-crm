from backend.src.backend.application.shared.errors import ApplicationError, NotFoundError, ConflictError


class UserError(ApplicationError):
    pass

class UserNotFoundError(NotFoundError, UserError):
    pass

class UsernameAlreadyExistsError(ConflictError, UserError):
    pass