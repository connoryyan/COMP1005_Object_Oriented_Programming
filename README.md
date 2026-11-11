# Project 1 Banking System

This log records the weekly code reviews of Project 1. For each review it lists the questions I asked, the feedback I received, the changes I implemented as a result, and the link between each change and what I learned from the discussion.

## Incremental development

Project 1 was developed incrementally (there are some evidences in the next section, and the very first implementation `implementation1.py` is included in this folder). The class diagram grew with the project as well (`UML1.png` -> `UML2.png` -> `UML3.png`). The largest structural step was splitting the original single-file implementation (`implementation1.py`) into one class per module (`account.py`, `branch.py`, `client.py`, `transaction.py`).

## Workshop 2-1 (10/8/2026)

Lance Feldman

- **Question:** In `process()` method in `Transaction` class, I was trying to add two parameter `account1` and `account2` to represent the 2 related accounts in this Transaction, and process the transaction by changing their account balance. But I think since related account is not a required attributes of `Transaction` class, maybe the class is not meant to responsible for actually handle the balance. So at the end I did not include that feature in `Transaction.process()`. Is it suppose to handle the balance? Or we can have another class. This might be better since the relationship between the 4 classes we currently have could be clearer without any complex referencing with each other.

    - **Answer:** For this course, we do not need to consider the actual control and modification of account balances at this stage. Our project is more like a simplified or toy version of a banking system. Having an additional class, such as a `TransactionManager`, to handle the processing of transactions would be a perfectly reasonable and convenient design. However, there is no single correct answer as to whether the responsibility for processing a transaction should belong to the `Transaction` object itself or to a separate manager class. Both approaches can be found in real-world banking systems, depending on the specific system design and requirements.

    - **Change in code & justifications:** The discussion confirmed that the involved accounts do **not** belong as attributes of `Transaction` (they are not "required attributes" of the class), and passing them in as arguments is not required for this project but is still a valid design used in real banking systems. But I finaly decided to keep the idea as a sort of interaction between classes. I therefore reworked `process()` to receive the accounts as parameters and actually move the money between them.

        **Before:**

        ```python
        def process(self) -> bool:
            if self.__status == "Cancelled":
                print("[INFO] The transaction cannot be completed.")
                return False
            # res = account1.withdrawal(self.__amount)
            # if not res:
            #     print("[INFO] The transaction cannot be completed.")
            #     return False
            # account2.deposit(self.__amount)
            self.__status = "Processed"
            print("[INFO] Transaction successful.")
            return True
        ```

        **After:**

        ```python
        def process(self, source: Account = None,
                    destination: Account = None) -> bool:
            if self.__status == "Cancelled":
                print("[INFO] The transaction cannot be completed.")
                return False
            if self.__status == "Processed":
                print("[INFO] The transaction has already been processed.")
                return False
            if source is not None and not source.withdrawal(self.__amount):
                print("[INFO] The transaction cannot be completed.")
                return False
            if destination is not None and not destination.deposit(self.__amount):
                print("[INFO] The transaction cannot be completed.")
                return False
            self.__status = "Processed"
            print("[INFO] Transaction successful.")
            return True
        ```
    - **Link to the learning experience:** I learned how to determine responsibility assignment and whether an operation belongs to the object itself or to a collaborator passed in as a parameter. I decided against adding a separate `TransactionManager` class because my tutor confirmed that both designs are valid, and this project is intended to be a simplified banking model and the smaller class graph is easier to maintain.


- **Question:** I know I could use docstring to clarify datatypes of parameters and return value, state their meanings, etc. But today we leant about how to use : and -> to relulate the datatype. Are they kind of overlap?

    - **Answer:** Docstrings are mainly used to explain the meaning, purpose, and other details of parameters and return values, while type hints such as : type and -> type provide a structured way to specify the expected data types. Python itself does not enforce type hints at runtime, but modern IDEs such as VS Code can use them for static analysis and highlight potential type errors, even when the code is syntactically valid. There are also dedicated static type-checking tools, such as *mypy*, *ty*, and *Pyrefly*, which can perform more thorough type checking.

    - **Change in code & justifications:** Following the discussion, every method now carries both a docstring (meaning and purpose of each parameter and return value) and type hints (`: type` on parameters, `-> type` on return values), e.g. `def deposit(self, amount: float) -> bool:`. The docstring explains the functionalities, meaning, and restrictions ("a positive amount of money"), while the type hint records the expected data type. Dedicated tools such as *mypy* are not used here because they are outside the course material; VS Code's built-in static analysis is sufficient for a project of this size.

    - **Link to the learning experience:** I learned that docstrings and type hints are actually complementary. Docstrings gives the meaning and purpose of each parameter and return value, while type hints restrict the datatypes so that IDEs can check statically. I now write both on every method, and use VS Code's built-in static analysis instead of external tools such as *mypy*, which are outside the course material.

- **Question:** In some method I wrote some `print()` of some information to let user know the result of their operations. But sometimes it can be annoying when too much information is showed in the terminal, or in some circumstances, the method is used as a module inside of another function, so that the those information could be confusing. How to deal with that.

    - **Answer:** Instead of using `print()` to display information from methods, we should use logging. And structured logging can provide a better way to record and manage this information. For example, Python libraries such as `structlog` can be used for structured logging, and the logs can be stored in formats such as `.csv` or `.json`. Tools such as *Grafana Loki* can then be used to collect and manage these logs.
    - **Change in code & justifications:** Tutor's suggestion to replace `print()` with structured logging libraries such as `structlog` (stored as `.csv`/`.json`, collected by Grafana Loki) is very useful and practical in real development. But it does **not apply** to this project since loggings are not actually part of the course and the rubric also forbids external libraries. Instead, I standardised all user-facing messages with a consistent `[INFO]` prefix (e.g. `print("[INFO] Withdrawal successful.")`), which keeps the terminal output uniform without external dependencies. I noted structured logging as the appropriate approach for real-world projects.


    - **Link to the learning experience:** I learned that `print()` is only suitable for quick feedback in a toy project, while real-world systems use structured logging so that logs can be collected, stored and queried. Although this project keeps the `[INFO]` print convention because external libraries are outside the course scope, I now understand when logging would be the appropriate choice.

## Workshop 3-1 (17/8/2026)

Lance Feldman

- **Question:** How to decide if a attribute should be private or public. In my opinion, balance is about privacy so it should be private, and the attributes of branchs are available to the publics so it should be public. Is it right?

    - **Answer:** Here might be a confusion between the privacy of information and whether an attribute should be public or private. When we say a attribute should be private, it means if we want to edit this attributes, we can only access it through a setter so that if it also affect other attributes in the class, we can update them. So for example we have phone number of a branch as a attribute, and it should be provate since if I edit the phone number here, it should also be updated in elsewhere.

    - **Change in code & justifications:** The discussion clarified that public/private is not about how sensitive the information is, but about whether changes to the attribute must be controlled through a setter. Before this review my attributes were a mix: I had already made money-related attributes such as `__balance` and contact details private, because they felt privacy-sensitive, while other attributes such as `name`, `accounts` and `preferred_branch` were still public.

        **Before:**

        ```python
        class Account:
            def __init__(self, id: int, typ: str):
                if isinstance(id, int): self.id: int = id
                if isinstance(typ, str): self.__type: str = typ
                self.__balance: float = 0.0

        class Client:
            def __init__(self, id: int, name: str, is_active: bool,
                         preferred_contact: str, contact: str):
                if isinstance(id, int): self.id: int = id
                if isinstance(name, str): self.name: str = name
                if isinstance(is_active, bool):
                    self.__is_active: bool = is_active
                if isinstance(preferred_contact, str):
                    self.__preferred_contact: str = preferred_contact
                if isinstance(contact, str): self.__contact = contact
                self.accounts: list[Account] = []
                self.preferred_branch: Branch = None
        ```

        **After:**
        Now every attribute except `id` is private and accessed through a getter/setter

        ```python
        def __init__(self, id: int, name: str, is_active: bool,
                     preferred_contact: str, contact: str):
            ...
            self.__name: str | None = name
            self.__is_active: bool = is_active
            self.__preferred_contact: str | None = preferred_contact
            self.__contact: str | None = contact
            self.__accounts: list[Account] = []
            self.__preferred_branch: Branch | None = None

        def get_name(self) -> str:
            return self.__name

        def set_name(self, name: str) -> None:
            if isinstance(name, str):
                self.__name = name
        ```

        When I was adding and reviewing every setter I caught a bug in `Branch.set_location()`, which was assigning to the wrong attribute:

        **Before:**

        ```python
        def set_location(self, location):
            if isinstance(location, str): self.__name = location
        ```

        **After:**

        ```python
        def set_location(self, location: str) -> None:
            if isinstance(location, str):
                self.__location = location
        ```

    - **Link to the learning experience:** I learned that public/private is a control decision and not about privacy. Making an attribute private means every change goes through its setter, so that related state can be updated consistently. Applying this rule made my attribute design uniform (only `id` stays public).

- **Question:** When writing the `Client.add_account()` and `Client.remove_account()`, should we reference a account by its id or by the whole object.

    - **Answer:** It depends. If we have all available account objects then we can easily reference a account by the whole object, but otherwise we will need to use IDs. But in a real project, if a account needs to be deleted, we probably still want to keep the information. So in that case we can use a `Client.deleted` attribute to record if this account is deleted so that we can delete it while keeping its information.

    - **Change in code & justifications:** Following the discussion, `add_account()` and `remove_account()` take the whole `Account` object rather than an id, because the integration test in `main.py` creates every account and passes it to the client directly:

        ```python
        def add_account(self, account: Account) -> None:
            if isinstance(account, Account) and account not in self.__accounts:
                self.__accounts.append(account)

        def remove_account(self, account: Account) -> None:
            if account in self.__accounts:
                self.__accounts.remove(account)
        ```

        Since a remove function is required, and since we don't have persistant storage for this project, Tutor's additional suggestion of a `deleted` flag to keep deleted accounts' information does **not apply** here. However, we do have a very close equivalent in the current design, which is the `is_active` flag on `Client`, which keeps the record while marking it inactive.

    - **Link to the learning experience:** I learned that object references are preferable to ids when all the objects are available in memory, and that ids only become necessary once the complete data is not available (for example in a database).

---

## Workshop 4-2 (3/9/2026)

Start project 2.
# Project 2


- Independent class for resource
- Dictionary to store different resources.
  ```py
  def __init__(self, 
                 necrotic_quant: int = 0, 
                 spirit_quant: int = 0, 
                 bone_quant: int = 0, 
                 flesh_quant: int = 0, 
                 ectoplasm_quant: int = 0):
        '''
        Initiate
        '''
        self.__resources = {
            "necrotic_runes": Resource(
                "Necrotic Runes",
                "Necrotic runes are a type of runes consisting of spirit," \
                " bone, flesh, and miasma runes.",
                necrotic_quant
            ), 
            "spirit_runes": Resource(
                "Spirit Runes",
                "Spirit Runes may be more important for spectral summons.",
                spirit_quant
            ),
            "bone_runes": Resource(
                "Bone Runes",
                "Bone Runes may be more important for skeletal summons.",
                bone_quant
            ),
            "flesh_runes": Resource(
                "Flesh Runes",
                "Flesh Runes may be more important for corpse-based summons.",
                flesh_quant
            ),
            "ectoplasm": Resource(
                "Ectoplasm",
                "Ectoplasm is a Necromancy material used to draw any alteration glyphs, and for conjuring.",
                ectoplasm_quant
            )
        }

        # self.__necrotic_runes = Resource(
        #     "Necrotic Runes",
        #     "Necrotic runes are a type of runes consisting of spirit," \
        #     " bone, flesh, and miasma runes.",
        #     necrotic_quant
        # )
        # self.__spirit_runes = Resource(
        #     "Spirit Runes",
        #     "Spirit Runes may be more important for spectral summons.",
        #     spirit_quant
        # )
        # self.__bone_runes = Resource(
        #     "Bone Runes",
        #     "Bone Runes may be more important for skeletal summons.",
        #     bone_quant
        # )
        # self.__flesh_runes = Resource(
        #     "Flesh Runes",
        #     "Flesh Runes may be more important for corpse-based summons.",
        #     flesh_quant
        # )
        # self.__ectoplasm = Resource(
        #     "Ectoplasm",
        #     "Ectoplasm is a Necromancy material used to draw any alteration glyphs, and for conjuring.",
        #     ectoplasm_quant
        # )
  ```
- Parameter selection for resourceManager.collect (list? dict? vars?)
  ```py
    def collect_resources(self, quantities: dict[str, Resource]):
        '''
        Add each resource by some quantity.

        Args:
            quantities (dict[str, Resource]): quantity of corresponding
              resource, e.g. {"spirit_runes": 4, ...}
        '''
        for key, num in quantities:
            if check_unsigned_int(num) and key in self.__resources.keys():
                self.__resources[key].add_quantity(num)
  ```

## Workshop 5-1 (7/9/2026)
- Sort of making a bad dicision since validation of a dictionary takes time and a lot of code

    ```py
    @staticmethod
    def input_to_dict(
        quantities: dict[str, int] | tuple[int, int, int, int, int]
    ) -> dict[str, int] | None:

        if isinstance(quantities, dict):
            items = quantities.items()

        elif isinstance(quantities, tuple):
            if len(quantities) != 5:
                return None

            items = zip(ResourceManager.KEYS, quantities)

        else:
            return None

        result = {}

        for key, num in items:
            if not (check_unsigned_int(num)
                    and key in ResourceManager.KEYS):
                return None

            result[key] = num

        return result
    ```
- use regular individual variable as parameter is recommneded, which involves a tradeoff.

## Workshop 6-2 (17/9/2026)

