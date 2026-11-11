"""Bank accounts with specialised rules and owned transaction records."""

from abc import ABC, abstractmethod
from math import isfinite

from .exceptions import (
    FinanceError, InsufficientFundsError, InvalidAmountError,
    MinimumBalanceError, WithdrawalLimitError,
)
from .transaction import Transaction


def is_finite_number(value) -> bool:
    """Accept finite integers and floats, excluding boolean values."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return isfinite(value)
    except OverflowError:
        return False


class Account(ABC):
    """Own the balance and ordered history of a single bank account.

    Public operations handle Finance errors before changing any state.
    last_error exposes the reason for a failed operation to its caller.
    """

    def __init__(self, id: int, name: str = "Account"):
        self.__id = (id if isinstance(id, int)
                     and not isinstance(id, bool) else None)
        self.__name = name if isinstance(name, str) else "Account"
        self._balance = 0.0
        self.__transactions: list[Transaction] = []
        self._last_error: FinanceError | None = None

    def __str__(self) -> str:
        return (f"{self.type} #{self.id}, Name: {self.name}, "
                f"Balance: ${self.balance:.2f}")

    def __repr__(self) -> str:
        return (f"{type(self).__name__}(id={self.id!r}, "
                f"name={self.name!r}, balance={self.balance!r})")

    def get_id(self) -> int | None:
        return self.__id

    id = property(get_id)

    def get_name(self) -> str:
        return self.__name

    name = property(get_name)

    def get_type(self) -> str:
        return type(self).__name__

    type = property(get_type)

    def get_balance(self) -> float:
        return self._balance

    balance = property(get_balance)

    @property
    def last_error(self) -> FinanceError | None:
        """Return the last handled error, or None after success."""
        return self._last_error

    def _validate_amount(self, amount) -> None:
        """Raise before an invalid amount can alter account state."""
        if not is_finite_number(amount) or amount <= 0:
            raise InvalidAmountError(
                f"Account {self.id}: invalid amount {amount!r}.")

    def deposit(self, amount: float) -> bool:
        """Deposit funds, handling invalid amounts within this class."""
        self._last_error = None
        try:
            self._validate_amount(amount)
            new_balance = self._balance + amount
            if not isfinite(new_balance):
                raise InvalidAmountError("Deposit exceeds numeric limits.")
        except FinanceError as error:
            self._last_error = error
            print(f"[INFO] {error}")
            return False
        self._balance = new_balance
        self.__create_transaction("Deposit", amount)
        return True

    def _check_withdrawal(self, amount: float) -> None:
        """Apply shared balance rules before completing a withdrawal."""
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Account {self.id}: ${amount:.2f} exceeds "
                f"balance ${self.balance:.2f}.")

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """Validate and handle a withdrawal using the concrete rules."""
        self._last_error = None
        try:
            self._validate_amount(amount)
            self._check_withdrawal(amount)
        except FinanceError as error:
            self._last_error = error
            print(f"[INFO] {error}")
            return False
        self._balance -= amount
        self.__create_transaction("Withdraw", amount)
        return True

    def get_transactions(self) -> list[Transaction]:
        """Return a copy of the ordered transaction collection."""
        return self.__transactions.copy()

    transactions = property(get_transactions)

    def get_transactions_filter(
        self, typ: str | None = None, status: str | None = None,
        amount_min: float | None = None,
        amount_max: float | None = None,
    ) -> list[Transaction]:
        """Filter history inclusively; invalid bounds leave it unchanged."""
        self._last_error = None
        try:
            for bound in (amount_min, amount_max):
                if bound is not None and not is_finite_number(bound):
                    raise InvalidAmountError("Invalid transaction bound.")
            if (amount_min is not None and amount_max is not None
                    and amount_min > amount_max):
                raise InvalidAmountError("Minimum exceeds maximum bound.")
        except FinanceError as error:
            self._last_error = error
            print(f"[INFO] {error}")
            return []
        return [
            t for t in self.__transactions
            if (typ is None or t.type == typ)
            and (status is None or t.status == status)
            and (amount_min is None or t.amount >= amount_min)
            and (amount_max is None or t.amount <= amount_max)
        ]

    def display_balance(self) -> None:
        print(f"Account {self.id} balance: ${self.balance:.2f}.")

    def __create_transaction(self, transaction_type: str,
                             amount: float) -> None:
        """Create a completed record only after a successful operation."""
        self.__transactions.append(Transaction(
            len(self.__transactions) + 1, transaction_type, amount,
            resulting_balance=self.balance, status="Processed",
        ))


class SavingsAccount(Account):
    """A savings account whose withdrawals preserve a minimum balance."""

    MINIMUM_BALANCE = 100.0

    def __init__(self, id: int, interest_rate: float,
                 name: str = "Savings"):
        super().__init__(id, name)
        self.__interest_rate = (
            interest_rate if is_finite_number(interest_rate)
            and 0 <= interest_rate <= 1 else 0.0)

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    interest_rate = property(get_interest_rate)

    def _check_withdrawal(self, amount: float) -> None:
        super()._check_withdrawal(amount)
        if self.balance - amount < self.MINIMUM_BALANCE:
            raise MinimumBalanceError(
                f"Account {self.id}: ${amount:.2f} would reduce "
                f"balance below ${self.MINIMUM_BALANCE:.2f}.")

    def withdraw(self, amount: float) -> bool:
        return super().withdraw(amount)


class EverydayAccount(Account):
    """An everyday account with a maximum single withdrawal."""

    MAX_WITHDRAWAL = 1000.0

    def __init__(self, id: int, name: str = "Everyday"):
        super().__init__(id, name)

    def _check_withdrawal(self, amount: float) -> None:
        if amount > self.MAX_WITHDRAWAL:
            raise WithdrawalLimitError(
                f"Account {self.id}: ${amount:.2f} exceeds "
                f"withdrawal limit ${self.MAX_WITHDRAWAL:.2f}.")
        super()._check_withdrawal(amount)

    def withdraw(self, amount: float) -> bool:
        return super().withdraw(amount)
