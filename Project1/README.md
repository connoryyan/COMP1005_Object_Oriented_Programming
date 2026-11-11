# Finance portfolio

From the repository root:

```powershell
python -m Project1.src.main
python -m pytest Project1/tests
```

Use a Python environment containing the packages in
`requirements-dev.txt`. In this workspace, the Miniconda interpreter has
these development tools installed.

## Design

`Account` is abstract. `SavingsAccount` preserves a minimum balance;
`EverydayAccount` enforces a single-withdrawal limit. Both reuse the shared
validation, balance update and transaction creation in `Account`.

Successful operations create `Processed` transaction records. Standalone
pending transactions may be processed or cancelled once. Failed operations
leave balances and transaction histories unchanged.

`Client` aggregates accounts in a dictionary keyed by integer account ID.
Accounts own an ordered list of transaction records. Collection properties
return shallow copies: callers cannot add or remove internal entries, while
individual account objects remain shared references.

Finance operations raise custom errors internally and catch them within the
responsible class. Account operations return `False` on failure and expose
`last_error`; a successful operation clears it. Missing client accounts
produce feedback and return `None`. Transaction filtering returns an empty
list and records an error if its bounds are invalid.

## Model and verification

The current model is `diagrams/current.uxf` (UMLet) or
`diagrams/current.puml` (PlantUML). Earlier models are retained as development
evidence. `main.py` demonstrates object interactions and recovery; pytest
provides the automated test suite.

From the repository root, generate the coverage report with:

```powershell
python -m pytest --cov=Project1/src --cov=Project2 --cov-report=term-missing --cov-report=html:reports/coverage --cov-report=xml:reports/coverage.xml
```

Coverage measures the implementation classes and supporting code. Test
modules and demonstration entry points are excluded by `.coveragerc`;
the demonstrations are nevertheless executed by regression tests.

Human workshop review records are in the repository-level `README.md`.
Unrecorded tutor conversations and historical development evidence must be
supplied from actual coursework; automated fixes do not replace them.
