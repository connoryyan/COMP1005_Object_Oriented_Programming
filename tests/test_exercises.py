"""Regression checks for the standalone exercise failures."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]


def test_random_example_runs():
    output = StringIO()
    with redirect_stdout(output):
        runpy.run_path(str(ROOT / "a.py"), run_name="__main__")
    assert len(output.getvalue().splitlines()) == 4


def test_tissue_quantity_failure_preserves_stock():
    with redirect_stdout(StringIO()):
        module = runpy.run_path(str(ROOT / "Q1/p5.py"))
    box = module["TissueBox"](3)
    tissue = module["Tissue"](2, "Plain", True)
    box.refill_maximum_tissues(tissue)
    for amount in (4, -1, 0, True, None, "2"):
        before = str(box)
        assert not box.take_multiple_tissues(amount)
        assert str(box) == before
    assert box.take_multiple_tissues(3)
    assert not box.take_single_tissue()
    assert not box.take_multiple_tissues(1)
