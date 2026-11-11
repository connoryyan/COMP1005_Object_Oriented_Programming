# Verification: 11 November 2026

Environment: Windows, Python 3.13.11 from
`C:/Users/Connor/miniconda3/python.exe`.

- Full pytest suite: **89 passed**.
- Core implementation statement coverage: **100% (639/639 statements)**.
- Project 1: all measured implementation modules reached 100%.
- Project 2: all measured implementation modules reached 100%.
- pycodestyle: passed for Project1/src, Project1/tests, Project2, Q1,
  ws1-1, a.py and the standalone exercise regression tests.
- All Python files passed syntax parsing.
- Both current UMLet models passed XML parsing.
- Finance and Necromancy demonstrations completed successfully.
- The original Necromancy manual test runner completed successfully.

Coverage excludes test files, main.py demonstration entry points and the
original Project2/test.py runner. The regression suite executes both main
functions in addition to testing business operations directly. This is
statement coverage, not a claim of exhaustive input or branch coverage.

## Reproduce from the repository root

```powershell
& 'C:/Users/Connor/miniconda3/python.exe' -B -m pytest -q --cov=Project1/src --cov=Project2 --cov-report=term-missing --cov-report=html:reports/coverage --cov-report=xml:reports/coverage.xml
& 'C:/Users/Connor/miniconda3/python.exe' -B -m pycodestyle Project1/src Project1/tests Project2 Q1 ws1-1 a.py tests
python -B -m Project1.src.main
python -B Project2/main.py
python -B Project2/test.py
```

The generated HTML coverage report is `coverage/index.html` and the
machine-readable report is `coverage.xml`. Captured demonstration output
is in finance-demo.txt and necromancy-demo.txt. The manual runner output
is in necromancy-manual-tests.txt.

Project 3 code is absent from this checkout. Human tutor reviews, the
Workshop 6-1 comparison artefacts and checkpoint feedback remain dependent
on the original coursework material. See ../DEVELOPMENT_NOTES.md.
