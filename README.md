## Workshop 2-1 
10/8/2026
Lance Feldman

- **Question:** In `process()` method in `Transaction` class, I was trying to add two parameter `account1` and `account2` to represent the 2 related accounts in this Transaction, and process the transaction by changing their account balence. But I think since related account is not a required attributes of `Transaction` class, maybe the class is not meant to responsible for actually handle the balance. So at the end I did not include that feature in `Transaction.process()`. Is it suppose to handle the balance? Or we can have another class. This might be better since the relationship between the 4 classes we currently have could be clearer without any complex referencing with each other.

    **Answer:** For this course, we do not need to consider the actual control and modification of account balances at this stage. Our project is more like a simplified or toy version of a banking system. Having an additional class, such as a `TransactionManager`, to handle the processing of transactions would be a perfectly reasonable and convenient design. However, there is no single correct answer as to whether the responsibility for processing a transaction should belong to the `Transaction` object itself or to a separate manager class. Both approaches can be found in real-world banking systems, depending on the specific system design and requirements.

- **Question:** I've been using python to develop some project so I know I could use docstring to clarify datatypes of parameters and return value, state their meanings, etc. But today we leant about how to use : and -> to relulate the datatype. Are they kind of overlap?

    **Answer:** Docstrings are mainly used to explain the meaning, purpose, and other details of parameters and return values, while type hints such as : type and -> type provide a structured way to specify the expected data types. Python itself does not enforce type hints at runtime, but modern IDEs such as VS Code can use them for static analysis and highlight potential type errors, even when the code is syntactically valid. There are also dedicated static type-checking tools, such as *mypy*, *ty*, and *Pyrefly*, which can perform more thorough type checking.

- **Question:** In some method I wrote some `print()` of some information to let user know the result of their operations. But sometimes it can be annoying when too much information is showed in the terminal, or in some circumstances, the method is used as a module inside of another function, so that the those information could be confusing. How to deal with that.

    **Answer:** Instead of using `print()` to display information from methods, we should use logging. And structured logging can provide a better way to record and manage this information. For example, Python libraries such as `structlog` can be used for structured logging, and the logs can be stored in formats such as `.csv` or `.json`. Tools such as *Grafana Loki* can then be used to collect and manage these logs.


## Workshop 3-1 
17/8/2026
Lance Feldman

- **Question:** How to decide if a attribute should be private or public. In my opinion, balance is about privacy so it should be private, and the attributes of branchs are available to the publics so it should be public. Is it right?
  
  **Answer:** Here might be a confusion between the privacy of information and whether an attribute should be public or private. When we say a attribute should be private, it means if we want to edit this attributes, we can only access it through a setter so that if it also affect other attributes in the class, we can update them. So for example we have phone number of a branch as a attribute, and it should be provate since if I edit the phone number here, it should also be updated in elsewhere.

- **Question:** When writing the `Client.add_account()` and `Client.remove_account()`, should we reference a account by its id or by the whole object.
- **Answer:** It depends. If we have all available account objects then we can easily reference a account by the whole object, but otherwise we will need to use IDs. But in a real project, if a account needs to be deleted, we probably still want to keep the information. So in that case we can use a `Client.deleted` attribute to record if this account is deleted so that we can delete it while keeping its information.