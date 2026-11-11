import pytest
from src.account import Account, SavingsAccount, EverydayAccount


class TestAccount:

    @pytest.fixture
    def savings_account(self):
        account = SavingsAccount(1, 0.05)
        account.deposit(500.0)
        return account

    @pytest.fixture
    def everyday_account(self):
        account = EverydayAccount(2)
        account.deposit(500.0)
        return account

    @pytest.fixture
    def accounts(self, savings_account, everyday_account):
        return [
            savings_account,
            everyday_account
        ]

    def test_deposit(self, accounts):
        for account in accounts:
            assert account.balance == pytest.approx(500.0)
            assert account.deposit(500.0)
            assert account.balance == pytest.approx(1000.0)
            assert len(account.transactions) == 2
            assert account.transactions[1].amount == pytest.approx(500.0)

    def test_invalid_deposit(self, accounts):
        invalid_amounts = [0, -100, True, False, "100", None]

        for account in accounts:
            original_balance = account.balance
            original_count = len(account.transactions)

            for amount in invalid_amounts:
                assert not account.deposit(amount)
                assert account.balance == pytest.approx(original_balance)
                assert len(account.transactions) == original_count

    def test_withdraw(self, accounts):
        accounts: list[Account] = accounts
        for account in accounts:
            assert account.balance == pytest.approx(500.0)
            assert account.withdraw(300.0)
            assert account.balance == pytest.approx(200.0)
            assert len(account.transactions) == 2
            assert account.transactions[1].amount == pytest.approx(300.0)

    def test_reject_invalid_withdraw(self, savings_account):
        amounts = [-50.0, 0.0, 600.0]
        for amount in amounts:
            before_balance = savings_account.balance
            before_count = len(savings_account.transactions)
            assert not savings_account.withdraw(amount)
            assert savings_account.balance == pytest.approx(before_balance)
            assert len(savings_account.transactions) == before_count

    def test_transactions_list_is_read_only(self, savings_account):
        original = len(savings_account.transactions)
        external = savings_account.transactions
        external.clear()
        assert len(external) == 0
        assert len(savings_account.transactions) == original

    def test_id_and_balance_cannot_be_assigned_directly(self, savings_account):
        with pytest.raises(AttributeError):
            savings_account.id = 99
        with pytest.raises(AttributeError):
            savings_account.balance = 9999.0
        assert savings_account.id == 1
        assert savings_account.balance == 500.0
