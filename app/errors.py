class DomainError(Exception):
    """Base class for buissnes rules violations."""


class ProfessorNotFoundError(DomainError):
    """Raised when a slot refears to a professor that doesnt exist"""
