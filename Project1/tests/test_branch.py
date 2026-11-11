"""Finance behaviour tests using class-local pytest fixtures."""

import pytest
from src.branch import Branch


class TestBranch:

    @pytest.fixture
    def branch(self):
        return Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)

    def test_close_branch(self, branch):
        assert branch.is_open
        branch.close()
        assert not branch.is_open

    def test_open_branch(self, ):
        branch = Branch(2, "Norwood", "Norwood", "08 8234 5678", False)
        assert not branch.is_open
        branch.open()
        assert branch.is_open
