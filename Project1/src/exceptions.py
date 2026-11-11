"""Exceptions raised and handled by Finance operations."""


class FinanceError(Exception):
    """Base class for Finance business errors."""


class InvalidAmountError(FinanceError):
    """The amount is not a positive, finite number."""


class InsufficientFundsError(FinanceError):
    """The account has insufficient funds."""


class MinimumBalanceError(FinanceError):
    """A withdrawal would violate the savings minimum."""


class WithdrawalLimitError(FinanceError):
    """A withdrawal exceeds the everyday account limit."""


class AccountNotFoundError(FinanceError):
    """The client does not own the requested account."""
