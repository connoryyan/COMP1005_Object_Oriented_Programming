# 1-1
Portfolio Exercise
Problem Statement

The Programming Portfolio begins in Workshop 1-2. No portfolio implementation is required during this workshop. Yippeee \(^ヮ^)/

The files created in Workshop 1-1 should still be retained as evidence of your preparation and early development practice.

# 1-2
Portfolio Exercise
Problem Statement

It is time to begin building your Programming Portfolio!! :D

 

A financial organisation requires a program that can represent its clients and financial accounts.

A client has information that identifies them and allows the organisation to contact them. An account has information that identifies the account, describes its purpose, and records its current balance.

The complete system will eventually manage more complex financial behaviour. During this workshop, you will create only the initial Client and Account classes and use them to construct several independent objects.

Your implementation should demonstrate:

    classes;
    attributes;
    methods;
    constructors;
    objects;
    self; and
    dot notation.

The project will be developed incrementally throughout the semester. Retain the code created during this workshop so it can be extended later.

 
Task 1: Plan the Initial Classes

Break the Finance problem into two initial classes: Client and Account.

Planning the responsibilities of each class before writing code helps prevent unrelated information and behaviour from being placed together.

 

Instructions

    Read the Finance Company scenario and identify the information that belongs to a client and the information that belongs to an account.
    Create a new folder for Project 1.
    Create a Python file for the initial Finance implementation.
    Read the Project 1 Scenario and identify the information that might belong to a client and an account.
        I recommend writing a few comments which describe the purpose of a Client object. This helps you plan your class
    Identify at least three attributes that describe one client.
    Your client attributes must include:
        A client number or identifier.
        A name.
        At least one form of contact information.
    Choose at least one additional client attribute that suits your version of the Finance project.
    Identify at least one useful behaviour that a client should perform.
    Create a heading for the Account class.
        I recommend writing a few comments which describe the purpose of a Client object. This helps you plan your class
    Identify at least three attributes that describe one account.
    Your account attributes must include:
        An account number or identifier.
        An account type.
        A balance.
     Choose at least one additional account attribute that suits your version of the Finance project.
    Identify at least two useful behaviours that an account should perform.
    Review the attributes and behaviours assigned to each class.
    Confirm that each item describes or acts upon the object represented by that class.

 

Planning Questions

    Does each attribute describe one specific object?
    Does each method represent something that object could reasonably do?
    Have any responsibilities been placed in the wrong class?
    Would two objects created from the class be able to contain different data?
    What choices make your Finance project different from another implementation?

Task 2: Create the Client Class

Create the first working version of the Client class.

 

Instructions

    Define a class named Client.
    Add a constructor using __init__().
    Add self as the first constructor parameter.
    Add a constructor parameter for each planned client attribute.
    Use self to assign each parameter to an object attribute.
    Ensure each attribute has a meaningful and consistent name.
    Define at least one method that uses or changes information belonging to the client.
    Add self as the first parameter of the method.
    Access the client’s attributes through self.
    Give the method a name that clearly describes the operation being performed.
    Run the file and correct any syntax or indentation errors.

 

Choose behaviour that suits your design. Examples include:

    Changing contact information.
    Changing a preferred contact method.
    Displaying selected client information.
    Recording whether the client is active.
    Performing another operation appropriate to a financial client.

Your method should interact with the attributes of the current object rather than operating only on unrelated values.

 

Notes

Please note, these interactions are important to grasp now but may not be used in your final implementation. We expect to see incremental development which may include adding and removing unused code.

 

 
Task 3: Create the Account Class

Create the first working version of the Account class.

 

Instructions

    Define a class named Account.
    Add a constructor using __init__().
    Add self as the first constructor parameter.
    Add a constructor parameter for each planned account attribute.
    Use self to assign each parameter to an object attribute.
    Include an attribute that stores the current account balance.
    Define a method that adds an amount to the balance.
    Add self as the first parameter of the method.
    Add a parameter that receives the amount being added.
    Update the balance using the current value stored in the object.
    Define a method that attempts to remove an amount from the balance.
    Add a parameter that receives the amount being removed.
    Check whether the account contains enough funds.
    Update the balance when sufficient funds are available.
    Display an appropriate message when the amount cannot be removed.
    Add at least one additional method or account behaviour based on your planning.
    Run the file and correct any syntax, indentation, or calculation errors.

 

Notes

    Complex validation is not required during this workshop.
    You may assume that the amounts provided to the methods are numbers.
    The balance should be changed through the object’s methods during your demonstration.
    Method names should describe the operation being performed.

Task 4: Create the Finance Objects

Create several objects from the Client and Account classes.

Each object should contain its own values while sharing the structure and behaviour defined by its class.

 

Instructions

    Create at least three Client objects.
    Give each client different attribute values.
    Use clear object names such as client_1, client_2, and client_3.
    Create at least three Account objects.
    Give each account different attribute values.
    Include different opening balances.
    Include at least two different account types.
    Use dot notation to access and print selected attributes from each object.
    Use dot notation to call the client method for at least two clients.
    Use dot notation to add funds to at least two accounts.
    Use dot notation to remove funds from at least two accounts.
    Attempt to remove more money than one account currently contains.
    Print the relevant balances before and after each operation.
    Confirm that changing one object does not change the attributes of another object.
    Retain this demonstration beneath the class definitions.

 

Demonstration Requirements

Your demonstration should clearly prove that:

    Multiple objects can be created from the same class.
    Each object stores independent attribute values.
    Constructor arguments determine the starting state of an object.
    Methods operate on the object used to call them.
    Dot notation can access attributes and invoke methods.

Do not hard-code the final balances. The displayed values should come from the attributes of the account objects.
Task 5: Test and Review the Initial Model

Review the Finance implementation and confirm that its behaviour matches your planning.

 

Instructions

    Run the complete Finance program.
    Confirm that every object is created without errors.
    Check that each object contains the values supplied to its constructor.
    Test every method at least twice.
    Test methods using different objects.
    Confirm that account calculations produce the expected balances.
    Confirm that an unsuccessful withdrawal does not incorrectly change the balance.
    Check that all attribute and method names are meaningful.
    Check that indentation is consistent.
    Remove temporary code that does not contribute to the final demonstration.
    Retain enough output to prove that the required classes, objects, attributes, and methods work.
    Save the completed code as the first implementation of Project 1.
    Retain your initial planning as evidence of how the program was developed.


# 2-1
Portfolio Exercise
Problem Statement

The first version of the Finance project contains Client and Account classes in a single Python file. The project now needs to be expanded and organised so that each class has a clearer responsibility.

During this workshop, you will separate the existing classes into modules and introduce two additional parts of the financial system:

    transactions that record individual financial activities; and
    branches that represent physical locations operated by the financial organisation.

Each class will remain reusable and independent. A separate main.py module will create instances and demonstrate their behaviour.
Task 1: Separate the Existing Classes into Modules

Reorganise the current Finance project so each class is stored in an appropriately named module.

 

Instructions

    Prepare the project folder.
        Retain the code completed during Workshop 1-2.
        Create a separate module for the Client class.
        Create a separate module for the Account class.
        Create a module named main.py.
    Move the existing class definitions.
        Place Client in client.py.
        Place Account in account.py.
        Retain the constructors, attributes, and methods already developed.
    Prepare the main module.
        Import both classes into main.py.
        Move the existing object creation and method calls into main.py.
        Run main.py and confirm that the program still behaves as it did previously.

 
Task 2: Create the Transaction Class

Create a class that represents one financial transaction. A transaction should record what occurred, its value, and its current processing status.

 

Instructions

    Create the class module.
        Create a module named transaction.py.
        Define a class named Transaction.
    Define the transaction data.
        Include attributes for:
            a transaction identifier;
            a transaction type;
            an amount;
            a description; and
            a status.
        Give new transactions a default status of "Pending".
    Add transaction behaviour.
        Allow a pending transaction to be processed.
        Allow a pending transaction to be cancelled.
        Allow the transaction description to be updated.
        Display appropriate feedback when an operation succeeds or cannot be completed.
    Test the class temporarily.
        Create at least two transaction objects.
        Process one transaction.
        Cancel another transaction.
        Confirm that each object retains its own status.

 

Notes

    A pending transaction may become "Processed".
    A pending transaction may become "Cancelled".
    A processed or cancelled transaction should not return to "Pending".
    Processing one transaction must not change another transaction.

 
Task 3: Create the Branch Class

Create a class that represents one branch of the financial organisation.

 

Instructions

    Create the class module.
        Create a module named branch.py.
        Define a class named Branch.
    Define the branch data.
        Include attributes for:
            a branch number;
            a branch name;
            a suburb or location;
            a phone number; and
            whether the branch is currently open.
        Set new branches to closed by default, while allowing a different starting value to be supplied.
    Add branch behaviour.
        Allow the branch to be opened.
        Allow the branch to be closed.
        Allow the branch phone number to be updated.
        Display suitable feedback after each operation.
    Test the class temporarily.
        Create at least two branch objects.
        Give them different locations and opening states.
        Change the state of one branch.
        Confirm that the other branch remains unchanged.

Task 4: Import the New Classes

Add the new modules to the main Finance program.

 

Instructions

    Prepare the class modules.
        Remove temporary object creation from:
            transaction.py;
            branch.py;
            client.py; and
            account.py.
        Keep only the relevant class definition in each module.
    Update main.py.
        Import all four classes:
            Client;
            Account;
            Transaction;
            Branch.

    Run main.py.
        Confirm that every import works.
        Resolve any module names, file locations, or import errors.

 
Task 5: Create and Test Instances

Use main.py to demonstrate that each class can create multiple independent instances.

 

Instructions

    Create client and account instances.
        Retain or revise the objects created during Workshop 1-2.
        Create at least three clients.
        Create at least three accounts.
    Create transaction instances.
        Create at least three transactions.
        Use different transaction types, amounts, descriptions, and statuses where appropriate.
    Create branch instances.
        Create at least three branches.
        Use different names, locations, phone numbers, and opening states.
    Demonstrate object methods.
        Update information belonging to a client.
        perform deposit and withdrawal operations using accounts.
        Process or cancel selected transactions.
        Open, close, or update selected branches.
    Demonstrate instance independence.
        Display relevant attributes before and after the method calls.
        Confirm that changing one object does not automatically change another instance of the same class.
        Use the object’s attributes to generate the displayed results rather than hard-coding the final values.

 
Task 6: Review the Expanded Model

Review the project structure and the responsibilities assigned to each class.

 

Instructions

    Review each module.
        Confirm that the module name matches the class it contains.
        Confirm that each module contains one class definition.
        Confirm that object creation occurs in main.py.
    Review each class.
        Check that its attributes describe the object it represents.
        Check that its methods operate on that object’s data.
        Replace names that do not clearly describe their purpose.
    Review the demonstration.
        Confirm that every class is used.
        Confirm that every required method is demonstrated.
        Remove temporary tests that duplicate the final demonstration.
        Retain enough evidence to show how the project has developed since Workshop 1-2. 

 
Task: Record Your Weekly Code Review

Complete an in-person code review during the workshop and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 

Instructions

    Create a code review record in the main folder of your project.
        Use either a README.md file or a clearly named text file such as code_reviews.txt.
        Use the same file throughout the semester so your reviews remain organised in one location.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 

Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 2-2
Portfolio Exercise
Project 1: Improving Output and Code Style
Problem Statement

The Finance project now contains separate modules for Client, Account, Transaction, and Branch. The main.py module imports these classes and creates several independent instances for testing.

The project is easier to navigate, but printing an object directly does not yet provide useful information. Each class will now be given string conversions that describe its objects and their current states.

You will also review the code style across the project and use autopep8 to correct common formatting issues. These changes should improve the readability of the project without changing its behaviour.

 
Task 1: Add Readable String Conversions

Add a __str__() method to each Finance class.

 

Instructions

    Add __str__() to Client.
        Return a readable description of the client.
        Include the client number, name, and preferred contact method.
    Add __str__() to Account.
        Return a readable description of the account.
        Include the account number, account name, account type, and current balance.
    Add __str__() to Transaction.
        Return a readable description of the transaction.
        Include the transaction identifier, type, amount, description, and current status.
    Add __str__() to Branch.
        Return a readable description of the branch.
        Include the branch number, name, location, phone number, and opening state.
    Review each method.
        Return the completed string rather than printing it.
        Use information stored by the current object.
        Ensure the output remains useful after an object’s state changes.

 

Notes

    The exact formatting is your decision.
    Currency values should be displayed consistently.
    Boolean values may be converted into more readable wording.
    Each returned string should clearly identify the object being displayed.

Task 2: Add Object Representations

Add a __repr__() method to each Finance class.

 

Instructions

    Create a representation for each class.
        Include the class name.
        Include enough attribute values to identify the object’s current state.
        Keep the representation concise and consistent.
    Review the difference between the conversions.
        Use __str__() for readable output.
        Use __repr__() for a more detailed representation of the object.
    Test each representation.
        Call repr() with at least one instance from each class.
        Confirm that the returned information reflects the current object state.

 

Notes

    The representation does not need to reproduce the constructor exactly.
    The output should make it clear which class created the object.
    State-changing attributes such as balance, transaction status, and branch opening state should be represented accurately.

Task 3: Update the Project Demonstration

Update main.py to demonstrate the new string conversions.

 

Instructions

    Display the initial objects.
        Print at least one object from each class directly.
        Confirm that Python uses the relevant __str__() method.
    Perform several object operations.
        Change selected client information.
        Complete account operations.
        Process or cancel selected transactions.
        Open or close selected branches.
    Display the updated objects.
        Print the affected objects again.
        Confirm that the output reflects their changed state.
        Print unaffected instances to demonstrate that they remain independent.
    Test the representations.
        Use repr() with at least one Client.
        Use repr() with at least one Account.
        Use repr() with at least one Transaction.
        Use repr() with at least one Branch.

 

Notes

    Use the instances created during Workshop 2-1.
    Additional instances are optional.
    Remove the long attribute-by-attribute print statements where printing the object now provides the same information.
    Retain enough output to demonstrate the required behaviour clearly.

Task 4: Apply Python Code Style

Review and format every module in Project 1.

 

Instructions

    Review the names used throughout the project.
        Use PascalCase for class names.
        Use lowercase names for module files.
        Use snake_case for methods, attributes, parameters, variables, and objects.
        Replace names that do not clearly describe their purpose.
    Review the formatting manually.
        Use four spaces for indentation.
        Include appropriate spacing around operators.
        Use blank lines consistently.
        Remove unnecessary whitespace.
        Check that the code remains readable.
    Run autopep8.
        Apply autopep8 to client.py.
        Apply autopep8 to account.py.
        Apply autopep8 to transaction.py.
        Apply autopep8 to branch.py.
        Apply autopep8 to main.py.
    Review the formatted project.
        Inspect the changes made by autopep8.
        Correct any naming or design issues that automatic formatting could not resolve.
        Run main.py again.
        Confirm that the project still behaves as expected.

 

Notes

    Automatic formatting improves presentation but does not assess whether the design is appropriate.
    Review every change rather than assuming that formatted code is correct.
    Retain the formatted files as the current version of Project 1.

Task: Record Your Weekly Code Review

Complete an in-person code review during the workshop and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 

Instructions

    Create a code review record in the main folder of your project.
        Use either a README.md file or a clearly named text file such as code_reviews.txt.
        Use the same file throughout the semester so your reviews remain organised in one location.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 

Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.
# 3-1
Portfolio Exercise

 
Project 1: Encapsulation and Relationships
Problem Statement

The Finance project now contains separate classes for clients, accounts, transactions, and branches. These classes work independently, but much of their data can still be accessed and changed directly. During this workshop, you will improve the design by protecting important object data, adding controlled access through getters and setters, and validating values before they are stored.

You will also create a UML class diagram of the current Finance system. The model will be used to identify how the classes could interact and where relationships should be introduced. The first relationships will then be implemented so the Finance project begins to behave as a connected object-oriented system rather than a collection of independent classes.
Task 1: Encapsulate the Existing Classes

Review the attributes in Client, Account, Transaction, and Branch and protect the data that should not be changed directly from outside the class.
Instructions

    Review all existing attributes.
        Decide which values represent internal object state.
        Change appropriate attributes from public to private.
        Update the class methods so they continue to access the correct attributes. (When renaming attributes press F2 or Fn + F2 on Mac to rename all elements so this will not be painful for you :P)
    Review main.py.
        Identify any code that directly accesses attributes that are now private.
        Remove or replace this direct access as the class interfaces are developed.
    Run the project.
        Confirm that each class can still be instantiated.
        Confirm that existing object methods continue to work.

Notes

    Most of the existing Finance attributes should now be private.
    An attribute becoming private does not automatically mean it requires both a getter and setter.
    Some values should only change through existing behaviours. For example, an account balance should continue to change through account operations.

 
Task 2: Add Getters and Setters

Provide controlled access to the private attributes.
Instructions

    Add getters where external code needs to read a value.
        Return the stored value.
        Keep the method focused on retrieving that value.
    Add setters where changing the value is appropriate.
        Allow client contact information to be updated.
        Allow suitable account information to be updated.
        Allow a transaction description to be updated.
        Allow suitable branch information to be updated.
    Retain behaviour-based changes where appropriate.
        Continue changing account balances through deposit() and withdraw().
        Continue changing transaction status through its processing methods.
        Continue changing branch opening state through its existing methods.
    Update main.py.
        Replace direct attribute access with getters and setters where required.
        Confirm that the resulting code still demonstrates the project clearly.

Notes

    Do not create a setter simply because a getter exists.
    Consider whether unrestricted changes would weaken the object’s design.

 
Task 3: Validate Object Data

Use isinstance() and appropriate conditions to prevent invalid values from replacing valid object state.
Instructions

    Review each constructor.
        Validate values before storing them.
        Check important strings, numbers, Boolean values, and identifiers.
        Provide a sensible starting value when invalid constructor data is supplied.
    Validate each setter.
        Confirm that replacement values use the expected data type.
        Prevent invalid values from replacing the existing value.
        Provide useful feedback when a change is rejected.
    Review existing object methods.
        Validate deposit and withdrawal amounts.
        Validate any other parameters where the expected data type is important.
    Test invalid values deliberately.
        Supply an incorrect type to several setters.
        Supply invalid numerical values to account operations.
        Confirm that the object remains in a valid state after each rejected operation.

Notes

    Remember that bool is considered an int by Python when using isinstance().
    Numeric validation may therefore need to distinguish Boolean values from genuine numbers.
    Validation should protect object state rather than only produce an error message.

 
Task 4: Model the Current Finance System

Create a UML class diagram representing the current state of Project 1.

Complete the first version of the model before adding relationships to the code.
Instructions

    Model the existing classes.
        Include Client.
        Include Account.
        Include Transaction.
        Include Branch.
    Represent the current class design.
        Include important attributes.
        Show their visibility.
        Include appropriate data types.
        Include the important methods.
        Show relevant parameters and return types.
    Examine the classes for possible relationships.
        Consider which objects naturally interact.
        Identify where one object may store or use another object.
        Identify whether each proposed relationship is association or aggregation.
        Add appropriate multiplicities.
    Review the model with your programming partner or workshop supervisor.
        Identify relationships that make sense.
        Identify relationships that feel forced or unnecessary.
        Correct any errors in the class responsibilities.

Notes

    The model should represent the current project rather than an imagined complete banking system.
    Not every possible relationship needs to be implemented.
    Retain this initial version so it can be compared with the updated model later.

 
Task 5: Implement the First Relationships

Use the reviewed model to introduce relationships between the existing Finance objects.
Instructions

    Add an aggregation between Client and Account.
        Allow a client to maintain multiple existing Account objects.
        Begin each client with no accounts.
        Add behaviour for adding an account.
        Add behaviour for removing an account.
        Provide controlled access to the client’s accounts.
    Protect the aggregation.
        Use isinstance() to ensure only Account objects can be added.
        Prevent the same account from being added more than once.
        Handle attempts to remove an account that is not assigned to the client.
    Demonstrate independent lifecycles.
        Create an account before assigning it to a client.
        Add the account to a client.
        Remove the account from that client.
        Confirm that the account object still exists.
    Add an association between Client and Branch.
        Allow a client to select a preferred branch.
        Begin each client without a preferred branch.
        Validate that the supplied object is a Branch.
        Allow the preferred branch to be changed.
    Demonstrate the association.
        Associate different clients with different branches.
        Change the preferred branch of one client.
        Confirm that the branch objects remain independent.

Notes

    A client may have zero or more accounts.
    A client may have no preferred branch or one preferred branch.
    The Account and Branch objects should exist independently from the client.
    The relationship methods should reject objects of the wrong type.

 
Task 6: Review the Model and Design

Compare the completed implementation with the UML model.
Instructions

    Update the UML diagram.
        Add the implemented aggregation.
        Add the implemented association.
        Update attributes and methods added during development.
        Check the visibility of each attribute.
        Confirm that multiplicities reflect the code.
    Compare the model with the implementation.
        Identify any differences.
        Decide whether the model or code should change.
        Ensure the final diagram accurately represents the current Finance project.
    Review class responsibilities.
        Check that Client manages client information and client relationships.
        Check that Account manages account information and balance behaviour.
        Check that Transaction manages transaction information and status.
        Check that Branch manages branch information and opening state.
    Review the applicable SOLID principles.
        Assess whether each class has one clear responsibility.
        Identify areas where unrelated responsibilities may have been introduced.
        Consider whether the current design could accommodate reasonable future changes without rewriting unrelated classes.

Notes

    Not every SOLID principle can be meaningfully applied at this stage of the course.
    Focus primarily on whether each class has a clear and focused responsibility.
    Do not introduce additional structures simply to satisfy a principle.
    Record any design issue that may need to be revisited as the project develops.

 
Task 7: Demonstrate the Updated Project

Update main.py so the current implementation clearly demonstrates the Topic 3 changes.
Instructions

    Demonstrate encapsulation.
        Read values using getters.
        Modify appropriate values using setters.
        Show that behaviour-based state changes still work.
    Demonstrate validation.
        Include several valid changes.
        Include several invalid changes.
        Confirm that rejected values do not corrupt the objects.
    Demonstrate the aggregation.
        Add different accounts to different clients.
        Attempt to add a duplicate.
        Attempt to add an invalid object.
        Remove an account and confirm that it still exists independently.
    Demonstrate the association.
        Select preferred branches for clients.
        Attempt to select an invalid object.
        Change an existing branch association.
    Retain clear evidence.
        Keep enough demonstration code to prove the required behaviour.
        Remove temporary tests that no longer contribute useful evidence.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 

Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.
# 3-2
Portfolio Exercise

 
Project 1: Encapsulation and Relationships
Problem Statement

The Finance project now contains separate classes for clients, accounts, transactions, and branches. These classes work independently, but much of their data can still be accessed and changed directly. During this workshop, you will improve the design by protecting important object data, adding controlled access through getters and setters, and validating values before they are stored.

You will also create a UML class diagram of the current Finance system. The model will be used to identify how the classes could interact and where relationships should be introduced. The first relationships will then be implemented so the Finance project begins to behave as a connected object-oriented system rather than a collection of independent classes.
Task 1: Encapsulate the Existing Classes

Review the attributes in Client, Account, Transaction, and Branch and protect the data that should not be changed directly from outside the class.
Instructions

    Review all existing attributes.
        Decide which values represent internal object state.
        Change appropriate attributes from public to private.
        Update the class methods so they continue to access the correct attributes. (When renaming attributes press F2 or Fn + F2 on Mac to rename all elements so this will not be painful for you :P)
    Review main.py.
        Identify any code that directly accesses attributes that are now private.
        Remove or replace this direct access as the class interfaces are developed.
    Run the project.
        Confirm that each class can still be instantiated.
        Confirm that existing object methods continue to work.

Notes

    Most of the existing Finance attributes should now be private.
    An attribute becoming private does not automatically mean it requires both a getter and setter.
    Some values should only change through existing behaviours. For example, an account balance should continue to change through account operations.

 
Task 2: Add Getters and Setters

Provide controlled access to the private attributes.
Instructions

    Add getters where external code needs to read a value.
        Return the stored value.
        Keep the method focused on retrieving that value.
    Add setters where changing the value is appropriate.
        Allow client contact information to be updated.
        Allow suitable account information to be updated.
        Allow a transaction description to be updated.
        Allow suitable branch information to be updated.
    Retain behaviour-based changes where appropriate.
        Continue changing account balances through deposit() and withdraw().
        Continue changing transaction status through its processing methods.
        Continue changing branch opening state through its existing methods.
    Update main.py.
        Replace direct attribute access with getters and setters where required.
        Confirm that the resulting code still demonstrates the project clearly.

Notes

    Do not create a setter simply because a getter exists.
    Consider whether unrestricted changes would weaken the object’s design.

 
Task 3: Validate Object Data

Use isinstance() and appropriate conditions to prevent invalid values from replacing valid object state.
Instructions

    Review each constructor.
        Validate values before storing them.
        Check important strings, numbers, Boolean values, and identifiers.
        Provide a sensible starting value when invalid constructor data is supplied.
    Validate each setter.
        Confirm that replacement values use the expected data type.
        Prevent invalid values from replacing the existing value.
        Provide useful feedback when a change is rejected.
    Review existing object methods.
        Validate deposit and withdrawal amounts.
        Validate any other parameters where the expected data type is important.
    Test invalid values deliberately.
        Supply an incorrect type to several setters.
        Supply invalid numerical values to account operations.
        Confirm that the object remains in a valid state after each rejected operation.

Notes

    Remember that bool is considered an int by Python when using isinstance().
    Numeric validation may therefore need to distinguish Boolean values from genuine numbers.
    Validation should protect object state rather than only produce an error message.

 
Task 4: Model the Current Finance System

Create a UML class diagram representing the current state of Project 1.

Complete the first version of the model before adding relationships to the code.
Instructions

    Model the existing classes.
        Include Client.
        Include Account.
        Include Transaction.
        Include Branch.
    Represent the current class design.
        Include important attributes.
        Show their visibility.
        Include appropriate data types.
        Include the important methods.
        Show relevant parameters and return types.
    Examine the classes for possible relationships.
        Consider which objects naturally interact.
        Identify where one object may store or use another object.
        Identify whether each proposed relationship is association or aggregation.
        Add appropriate multiplicities.
    Review the model with your programming partner or workshop supervisor.
        Identify relationships that make sense.
        Identify relationships that feel forced or unnecessary.
        Correct any errors in the class responsibilities.

Notes

    The model should represent the current project rather than an imagined complete banking system.
    Not every possible relationship needs to be implemented.
    Retain this initial version so it can be compared with the updated model later.

 
Task 5: Implement the First Relationships

Use the reviewed model to introduce relationships between the existing Finance objects.
Instructions

    Add an aggregation between Client and Account.
        Allow a client to maintain multiple existing Account objects.
        Begin each client with no accounts.
        Add behaviour for adding an account.
        Add behaviour for removing an account.
        Provide controlled access to the client’s accounts.
    Protect the aggregation.
        Use isinstance() to ensure only Account objects can be added.
        Prevent the same account from being added more than once.
        Handle attempts to remove an account that is not assigned to the client.
    Demonstrate independent lifecycles.
        Create an account before assigning it to a client.
        Add the account to a client.
        Remove the account from that client.
        Confirm that the account object still exists.
    Add an association between Client and Branch.
        Allow a client to select a preferred branch.
        Begin each client without a preferred branch.
        Validate that the supplied object is a Branch.
        Allow the preferred branch to be changed.
    Demonstrate the association.
        Associate different clients with different branches.
        Change the preferred branch of one client.
        Confirm that the branch objects remain independent.

Notes

    A client may have zero or more accounts.
    A client may have no preferred branch or one preferred branch.
    The Account and Branch objects should exist independently from the client.
    The relationship methods should reject objects of the wrong type.

 
Task 6: Review the Model and Design

Compare the completed implementation with the UML model.
Instructions

    Update the UML diagram.
        Add the implemented aggregation.
        Add the implemented association.
        Update attributes and methods added during development.
        Check the visibility of each attribute.
        Confirm that multiplicities reflect the code.
    Compare the model with the implementation.
        Identify any differences.
        Decide whether the model or code should change.
        Ensure the final diagram accurately represents the current Finance project.
    Review class responsibilities.
        Check that Client manages client information and client relationships.
        Check that Account manages account information and balance behaviour.
        Check that Transaction manages transaction information and status.
        Check that Branch manages branch information and opening state.
    Review the applicable SOLID principles.
        Assess whether each class has one clear responsibility.
        Identify areas where unrelated responsibilities may have been introduced.
        Consider whether the current design could accommodate reasonable future changes without rewriting unrelated classes.

Notes

    Not every SOLID principle can be meaningfully applied at this stage of the course.
    Focus primarily on whether each class has a clear and focused responsibility.
    Do not introduce additional structures simply to satisfy a principle.
    Record any design issue that may need to be revisited as the project develops.

 
Task 7: Demonstrate the Updated Project

Update main.py so the current implementation clearly demonstrates the Topic 3 changes.
Instructions

    Demonstrate encapsulation.
        Read values using getters.
        Modify appropriate values using setters.
        Show that behaviour-based state changes still work.
    Demonstrate validation.
        Include several valid changes.
        Include several invalid changes.
        Confirm that rejected values do not corrupt the objects.
    Demonstrate the aggregation.
        Add different accounts to different clients.
        Attempt to add a duplicate.
        Attempt to add an invalid object.
        Remove an account and confirm that it still exists independently.
    Demonstrate the association.
        Select preferred branches for clients.
        Attempt to select an invalid object.
        Change an existing branch association.
    Retain clear evidence.
        Keep enough demonstration code to prove the required behaviour.
        Remove temporary tests that no longer contribute useful evidence.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 

Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.
# 4-1
Portfolio Exercise
Project 2: Necromancy Game
Problem Statement

Project 2 is a game-inspired object-oriented system based around a necromancer summoning and controlling undead creatures. A necromancer gathers magical resources that can be consumed when performing summoning rituals. Every ritual requires Ectoplasm, while different undead require different combinations of Necrotic Runes, Spirit Runes, Bone Runes, and Flesh Runes. Summoned undead begin at Level 1 with their own starting health and power. They can later be levelled to improve these statistics. The focus of this workshop is establishing the first model and implementation of this system using the concepts introduced so far. The project will continue to develop as new object-oriented concepts are introduced.

 

Important Notice

The tasks written in 4-1 are lengthy and you may not finish them during this workshop. This is okay!! :D

These tasks are a combination of all topics up until this point. If you need additional time, please ensure you are utilising both classes and your additional 4 hours of study per week to make up 10 hours of study. 
Task 1: Model Project 2

Create the first UML class diagram for Project 2 before beginning the implementation.
Instructions

    Identify the main objects required by the current summoning system.
        Include an object responsible for managing resources.
        Include a SummoningRitual.
        Include an Undead.
        Include a Necromancer in the future structure of the model.
    Identify the important attributes.
        Include resource quantities.
        Include ritual costs.
        Include undead identifiers and statistics.
        Include level where appropriate.
        Apply private visibility to object state.
    Identify the current and planned behaviours.
        Include collecting and spending resources.
        Include checking ritual requirements.
        Include creating undead.
        Include levelling undead.
        Include planned summoning behaviour for the necromancer.
    Identify the relationships that will be required.
        Identify where object attributes may be used.
        Identify where composition may be appropriate.
        Identify any aggregation or association relationships that may be required.
        Include appropriate multiplicities.
    Review the responsibilities of the proposed classes.
        Keep resource management with the resource object.
        Keep ritual requirements with the ritual.
        Keep undead statistics and levelling with the undead.
        Avoid assigning every responsibility to the necromancer.

Notes

    The UML model represents both the current implementation and the direction the project is expected to take.
    Some relationships identified in this task will not be implemented until later workshops.
    Retain the model because it will continue to change as new OOP concepts are introduced.

 
Task 2: Implement the Resource System

Create the class responsible for managing resources used during summoning.

 
Instructions

    Store the five resources used by Project 2.
        Necrotic Runes.
        Spirit Runes.
        Bone Runes.
        Flesh Runes.
        Ectoplasm.
    Make each resource quantity private.
        Use integer quantities.
        Prevent quantities from beginning below 0.
    Provide read-only properties for each resource.
    Add behaviour for collecting resources.
        Allow several resource quantities to be supplied in one operation.
        Validate each quantity.
        Prevent invalid values from changing the object state.
    Add behaviour for checking resource requirements.
        Receive the required quantities.
        Return whether all required resources are currently available.
    Add behaviour for spending resources.
        Check all requirements before changing any values.
        Consume the required resources when enough are available.
        Prevent any resource from falling below 0.
    Add a constant representing the minimum valid resource quantity.
    Add a string conversion that clearly displays the available resources.

Notes

    Resource quantities should change through behaviours rather than direct assignment.
    A failed operation should leave all existing quantities unchanged.

 
Task 3: Implement the Initial Undead

Create the initial class used to represent summoned undead.

 
Instructions

    Define the private attributes.
        Unit identifier.
        Name.
        Health.
        Power.
        Level.
    Begin every undead creature at Level 1.
    Add constants defining the current stat boundaries.
        Minimum health.
        Maximum health.
        Minimum power.
        Maximum power.
        Maximum level.
    Add constants defining stat growth.
        Health gained per level.
        Power gained per level.
    Provide read-only properties for the undead state.
    Add behaviour for levelling.
        Increase the level.
        Increase health.
        Increase power.
        Prevent health and power from exceeding their maximum values.
        Prevent the undead from exceeding the maximum level.
    Add a string conversion.
        Include the identifier.
        Include the undead name.
        Include the level.
        Include current and maximum health.
        Include current and maximum power.

 
Task 4: Implement Summoning Rituals

Create the class responsible for describing the requirements and result of a summoning ritual.

 
Instructions

    Store information about the ritual.
        Ritual name.
        Name of the undead it creates.
        Starting health.
        Starting power.
    Store the resource requirements.
        Necrotic Rune cost.
        Spirit Rune cost.
        Bone Rune cost.
        Flesh Rune cost.
        Ectoplasm cost.
    Ensure every ritual requires Ectoplasm.
        Other Rune costs may be 0.
        Different rituals should use different combinations of resources.
    Add appropriate read-only properties.
    Add behaviour for checking whether the ritual can be performed.
        Require a valid resource object.
        Check all resource requirements.
        Return whether the ritual can currently be performed.
    Add behaviour for consuming the required resources.
        Delegate the resource changes to the resource object.
        Return whether the operation succeeded.
    Add behaviour for creating an undead object.
        Receive an identifier.
        Use the ritual's summon information and starting statistics.
        Return the newly created Undead.
    Create at least four ritual objects.
        Undead Skeleton Warrior.
        Vengeful Ghost.
        Putrid Zombie.
        Phantom Guardian.

Notes

    Bone Runes may be more important for skeletal summons.
    Spirit Runes may be more important for spectral summons.
    Flesh Runes may be more important for corpse-based summons.
    More powerful summons should generally require more resources.

 
Task 5: Demonstrate the Initial Project 2 Classes

Create a small demonstration showing that the independent classes created in this workshop work correctly.

 
Instructions

    Create a resource object with an initial collection of Runes and Ectoplasm.
    Create several summoning rituals.
        Give each ritual different resource requirements.
        Give each resulting undead different starting statistics.
    Display the current resources.
    Check whether selected rituals can currently be performed.
    Create an Undead object using one of the rituals.
        Assign it an identifier.
        Display the resulting object.
    Level the undead creature.
        Display it before levelling.
        Level it once.
        Display its updated state.
    Compare the current implementation with the UML model.
        Confirm that implemented classes match the model.
        Retain planned relationships that will be implemented later.
        Correct accidental differences.

 
Notes

    Do not connect the complete summoning system yet.
    The Necromancer will coordinate these objects in the next workshop.
    The purpose of this demonstration is to confirm that the individual parts are ready to be connected.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 

Instructions

    Use the code review record in the main folder of your project. Ensure you add a heading now for each project. You do not need to review both projects but to allow us to see which were reviewed at the time if it is not obvious upon first glance.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.
# 4-2
Portfolio Exercise
Problem Statement

Project 2 now has the main classes required for summoning, but they still need to operate as one connected system. In this workshop, you will complete the Necromancer, implement the composition with its resources, connect rituals and undead through summoning, and demonstrate the resulting object model.

You will also make a smaller refinement to Project 1 by applying properties and introducing composition between Account and the transaction records it creates.

 
Task 1: Complete the Necromancer

The main Project 2 classes were created during Workshop 4-1. Connect them by implementing the Necromancer and its relationships.
Instructions

    Create the Necromancer class.
        Include a private name.
        Include a private resource object.
        Include a private collection of controlled undead.
        Include a value used to assign identifiers to new summons.
    Compose the resource object.
        Create the resource-management object inside the Necromancer constructor.
        Delegate resource changes to the resource object.
    Add a constant representing the maximum number of undead that can be controlled.
    Implement summoning.
        Require a SummoningRitual.
        Confirm that the necromancer has enough resources.
        Perform the ritual.
        Create the resulting undead.
        Add successful summons to the controlled collection.
        Assign each summon a unique identifier.
    Implement dismissing.
        Find an undead creature using its identifier.
        Remove it from the controlled collection.
        Return whether the operation succeeded.
    Create a private helper method for locating a controlled summon.
        Use the helper when dismissing undead.
        Reuse it anywhere else an undead object needs to be found by identifier.
    Allow a controlled summon to be levelled by identifier.
        Find the required undead using the helper method.
        Delegate the level change to the undead object.

Notes

    The Necromancer creates and owns its resource object, making this a composition relationship.
    The necromancer coordinates objects but should not directly manipulate their private state.

 
Task 2: Demonstrate the Connected Summoning System

Update the Project 2 demonstration so that it proves the completed Topic 4 object model works.
Instructions

    Create a necromancer with an initial collection of resources.
    Create several summoning rituals.
        Include the Undead Skeleton Warrior.
        Include the Vengeful Ghost.
        Include the Putrid Zombie.
        Include the Phantom Guardian.
        Give each ritual different Rune requirements.
        Require Ectoplasm for every ritual.
    Perform several successful summons.
        Confirm that resources are consumed.
        Confirm that undead are added to the controlled collection.
    Attempt a ritual that cannot currently be performed.
        Confirm that the summon does not occur.
        Confirm that resources remain valid.
    Collect additional resources and perform the ritual again.
    Level one controlled undead creature.
        Display its state before levelling.
        Level it through the necromancer.
        Display its updated state.
    Dismiss one controlled undead creature.
        Confirm that it is removed from the necromancer's army.
    Display the completed necromancer.
        Include its remaining resources.
        Include its remaining controlled undead.
    Compare the implementation with the Project 2 UML model.
        Add the completed Necromancer.
        Add its composition relationship with the resource object.
        Confirm the other relationships and multiplicities.
        Correct any differences between the model and implementation.

Notes

    The undead do not need to interact with one another.

 
Task 3: Refine Project 1 with Properties and Composition

Return briefly to Project 1 and apply the Topic 4 concepts to its existing design.

 
Instructions

    Review the existing getters and setters.
        Convert suitable accessors to properties.
        Keep identifiers and other fixed values read-only.
        Keep balances and state changes controlled by behavioural methods where appropriate.
    Update external code to use property syntax.
        Replace direct getter calls where a property now exists.
        Confirm that private attributes remain protected.
    Add a transaction collection to Account.
        Store the transaction records created by that account.
        Provide controlled read access to the collection.
    Make Account responsible for creating transaction records.
        Create a transaction after a successful deposit.
        Create a transaction after a successful withdrawal.
        Record useful information such as the transaction type, amount, and resulting balance.
    Use a private helper method to create transaction records.
        Reuse the helper from both deposit and withdrawal behaviour.
        Assign each transaction an identifier.
    Review the relationship.
        Transaction objects should be created by the account rather than independently in main.py.
        Update the UML model to represent the new composition.
    Demonstrate the change.
        Make at least one deposit.
        Make at least one withdrawal.
        Display the resulting transaction records.
        Confirm that invalid financial operations do not create transaction records.

 
Notes

    The Account–Transaction relationship is now composition because the account creates and owns its transaction records.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 

Instructions

    Use the code review record in the main folder of your project. Ensure you add a heading now for each project. You do not need to review both projects but to allow us to see which were reviewed at the time if it is not obvious upon first glance.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.
# 5-1
Portfolio Exercise
Project 1: Specialising Accounts
Problem Statement

Project 1 currently represents every bank account using the same Account class. While all accounts share common information and behaviours, different account types may place different rules around how that behaviour works.

In this workshop, you will redesign the existing account structure using inheritance. Account will provide the common state and behaviour, while specialised account classes will extend or override that behaviour where their requirements differ.

Begin by updating the UML model before changing the implementation.

 
Task 1: Model the Account Inheritance Hierarchy

Update the Project 1 UML class diagram to introduce inheritance.

 
Instructions

    Review the existing Account class.
        Identify attributes that apply to every type of account.
        Identify behaviours that should be available to every account.
        Identify existing relationships that should continue to use Account.
    Model Account as the generalisation.
        Retain the common account state.
        Retain common behaviours such as depositing and withdrawing.
        Retain the composition with transaction records.
    Add at least two specialised account classes.
        Include a SavingsAccount.
        Include an EverydayAccount.
    Identify specialised state and behaviour.
        Give SavingsAccount an interest rate.
        Give SavingsAccount a minimum balance requirement.
        Give EverydayAccount a maximum amount that can be withdrawn in a single operation.
        Identify which behaviour will need to be overridden.
    Add the inheritance relationships to the UML model.
        Use generalisation notation.
        Keep the existing Client relationship with the general Account class.
        Retain the Account composition with Transaction.
    Review the existing account type attribute.
        Consider whether it still provides useful information once account type is represented through specialised classes.
        Keep or remove it based on your design.
        Ensure the UML model and implementation remain consistent.

 
Notes

    Account represents the common features shared by all account types.
    SavingsAccount and EverydayAccount represent more specialised forms of that general concept.
    Model the hierarchy before modifying the implementation.

Task 2: Refactor Account as the Parent Class

Prepare the existing Account class to support specialised child classes.

 
Instructions

    Review the common account attributes.
        Keep attributes shared by every account in Account.
        Change appropriate private attributes to protected visibility where subclasses require direct access.
        Keep attributes private where subclasses do not require access.
    Retain the common account properties.
        Account number should remain read-only.
        Balance should remain read-only from outside the object.
        Transaction records should remain accessible without allowing the collection to be replaced directly.
    Retain the common account behaviours.
        Deposit funds.
        Withdraw funds.
        Record successful transactions.
    Keep transaction creation within Account.
        Successful deposits should continue to create transaction records.
        Successful withdrawals should continue to create transaction records.
        Failed operations should not create transactions.
    Review methods used by future subclasses.
        Identify which behaviours can be inherited unchanged.
        Identify which behaviours will need to be overridden.

 
Notes

    Protected visibility is useful when subclasses need controlled access to inherited state.
    Common behaviour should remain in the parent rather than being copied into each child class.

Task 3: Implement the Specialised Accounts

Create the specialised account classes represented in the updated UML model.

 
Instructions

    Create SavingsAccount.
        Inherit from Account.
        Add an interest rate.
        Provide appropriate property access.
        Add a constant representing the minimum balance that must remain in the account.
    Use super() in the SavingsAccount constructor.
        Pass the common account information to the Account constructor.
        Initialise only specialised state inside SavingsAccount.
    Override withdraw() in SavingsAccount.
        Apply the minimum balance requirement before allowing the withdrawal.
        Reject withdrawals that would reduce the account below its minimum balance.
        Use the parent implementation to complete valid withdrawals.
    Create EverydayAccount.
        Inherit from Account.
        Add a constant representing the maximum amount permitted in a single withdrawal.
    Use super() in the EverydayAccount constructor.
    Override withdraw() in EverydayAccount.
        Reject withdrawals above the specialised limit.
        Use the parent implementation for valid withdrawals.
    Review duplicated code.
        Keep common validation, balance changes, and transaction recording in Account.
        Do not copy the complete parent withdraw() implementation into each subclass.

 
Notes

    Overriding allows a child class to change part of an inherited behaviour.
    Calling super().withdraw() allows the specialised class to add its own rule while retaining the common withdrawal behaviour.
    The child constructors should initialise inherited state through super() rather than assigning the parent's attributes themselves.

 
Task 4: Integrate the Inheritance Hierarchy

Update the rest of Project 1 so that it works with the new account hierarchy.

 
Instructions

    Create several account objects.
        Create at least one SavingsAccount.
        Create at least one EverydayAccount.
    Add the specialised accounts to a Client.
        Confirm that the existing relationship accepts each specialised account as an Account.
        Confirm that the client can contain different account types in the same collection.
    Demonstrate inherited behaviour.
        Deposit into each account.
        Display their balances.
        Display the resulting transaction records.
    Demonstrate overridden behaviour.
        Complete a valid withdrawal from a savings account.
        Attempt a withdrawal that violates its minimum balance.
        Complete a valid withdrawal from an everyday account.
        Attempt a withdrawal above its maximum withdrawal amount.
    Demonstrate isinstance().
        Confirm that a SavingsAccount is an Account.
        Confirm that an EverydayAccount is an Account.
        Confirm that the specialised objects retain their own concrete types.
    Compare the completed implementation with the UML model.
        Confirm that the inheritance hierarchy matches.
        Confirm that protected and private visibility are represented correctly.
        Confirm that existing aggregation and composition relationships remain accurate.
        Correct any accidental differences.

 
Notes

    A Client should not need separate logic for every account subtype.
    Inheritance allows the existing Account relationship to support specialised account objects.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 5-2
Portfolio Exercise
Problem Statement

Project 2 currently represents every summoned creature using the same Undead class. Although this provides common behaviour, the different summons now need their own statistics and specialised behaviours.

In this workshop, refactor the existing undead design into an inheritance hierarchy. Keep Undead as the generalisation, introduce broader undead specialisations, and represent the existing summons using specialised classes.

 
Task 1: Model the Undead Inheritance Hierarchy

Update the Project 2 UML class diagram before changing the implementation.

 
Instructions

    Keep Undead as the general parent class.
        Retain the state and behaviour shared by all undead.
        Retain levelling behaviour.
        Retain the existing minimum and maximum stat structure.
    Add two intermediate specialisations.
        WarriorUndead.
        CursedUndead.
    Add the existing summon types to the hierarchy.
        SkeletonWarrior inherits from WarriorUndead.
        PhantomGuardian inherits from WarriorUndead.
        VengefulGhost inherits from CursedUndead.
        PutridZombie inherits directly from Undead.
    Review the visibility of the existing Undead attributes.
        Keep state private when subclasses do not require direct access.
        Change appropriate attributes to protected where inherited behaviour requires access.
    Add a command() behaviour to the hierarchy.
        Include the general behaviour in Undead.
        Show overridden versions where specialised behaviour is required.
    Retain the existing relationships with:
        Necromancer.
        SummoningRitual.
        ResourcePool.

 
Notes

    Do not introduce multiple inheritance yet.
    The hierarchy should represent the summons already used by Project 2.
    The existing object relationships should remain intact while inheritance is added.

 
Task 2: Implement the Undead Hierarchy

Refactor the existing Undead implementation and create the specialised undead classes.

 
Instructions

    Retain the common functionality in Undead.
        Identifier.
        Name.
        Health.
        Power.
        Level.
        Levelling behaviour.
        Stat limits.
    Add a general command() method to Undead.
        Provide behaviour suitable for any undead creature.
    Create WarriorUndead.
        Inherit from Undead.
        Use super() in its constructor.
        Override command() with behaviour suitable for a warrior.
        Use super() within the overridden method to retain useful parent behaviour.
    Create CursedUndead.
        Inherit from Undead.
        Use super() in its constructor.
        Override command() with behaviour suitable for a cursed undead.
        Retain useful parent behaviour using super().
    Create the four specialised summons.
        SkeletonWarrior.
        VengefulGhost.
        PutridZombie.
        PhantomGuardian.
    Use super() from each specialised constructor.
        Pass common information through the inheritance hierarchy.
        Avoid recreating inherited attributes inside the specialised classes.
    Give each specialised summon its own stat boundaries.
        Preserve the different starting strengths established earlier in Project 2.
        Provide appropriate minimum and maximum health.
        Provide appropriate minimum and maximum power.
        Continue using the inherited levelling behaviour.

 
Notes

    The parent class should contain behaviour that genuinely applies to all undead.
    Specialised classes should contain only the differences that make that summon type distinct.
    Avoid copying the complete Undead implementation into the child classes.

 
Task 3: Connect Specialised Summons to the Existing System

Update the existing summoning system so rituals create the new specialised undead objects.

 
Instructions

    Update SummoningRitual so that a ritual identifies the specialised summon class it creates.
    Update create_summon().
        Create the appropriate specialised undead object.
        Continue assigning the identifier supplied by the Necromancer.
    Update the existing rituals.
        The Skeleton Warrior ritual creates a SkeletonWarrior.
        The Vengeful Ghost ritual creates a VengefulGhost.
        The Putrid Zombie ritual creates a PutridZombie.
        The Phantom Guardian ritual creates a PhantomGuardian.
    Retain the existing resource requirements.
        Continue using the Rune and Ectoplasm costs established in Topic 4.
        Do not change the resource-management responsibilities.
    Demonstrate the updated system.
        Successfully summon several different specialised undead.
        Confirm that each object is an Undead.
        Confirm that each object retains its specialised type.
        Level at least one summon using the existing levelling behaviour.
        Call command() on different summon types and observe the overridden behaviour.
    Compare the implementation with the updated UML model.
        Confirm the inheritance relationships.
        Confirm protected and private visibility.
        Confirm the existing composition, aggregation, and association relationships remain accurate.

 
Notes

    The purpose of this task is to integrate inheritance into the existing system rather than redesign the summoning process.
    The Necromancer should still coordinate summoning rather than directly creating each specialised undead itself.
    Resource management remains the responsibility of ResourcePool.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 6-1
Portfolio Exercise
Project 1: Review, Refine and Evaluate
Problem Statement

Your portfolio has already reached its first major checkpoint. Before adding further complexity, use this workshop to review the feedback received and improve the existing system.

You will also complete an AI literacy exercise using code you have already developed independently. The aim is not to replace your solution with generated code, but to investigate how the quality of a prompt affects the response produced and how generated solutions should be critically evaluated before they are trusted.

 
Task 1: Respond to Checkpoint Feedback

Review the feedback received for Project 1 and identify meaningful changes to make before continuing development.

 
Instructions

    Review your Project 1 checkpoint feedback.
        Identify issues relating to the object model.
        Identify issues relating to class responsibilities.
        Identify issues relating to relationships.
        Identify issues relating to encapsulation or visibility.
        Identify issues relating to inheritance.
        Identify issues relating to code quality or readability.
    Select the feedback that requires changes to the project.
    Implement the required changes.
        Correct structural problems before adding new functionality.
        Update affected classes and methods.
        Keep existing behaviour working where it is still appropriate.
    Update the UML model where the structure has changed.
        Keep the model consistent with the implementation.
        Correct relationships, multiplicities, visibility, or inheritance where required.
    Re-run the Project 1 demonstration.
        Confirm that the corrected system still operates as expected.
        Correct any problems introduced during the changes.
    Record the most important change in your code review notes. Please do your code review on these notes.
        Identify the feedback.
        Describe the resulting change.
        Explain why the revised design is stronger.

 
Notes

    Different projects will require different changes because checkpoint feedback will vary.
    Prioritise structural and conceptual issues over cosmetic changes.

 
Task 2: Create a Baseline AI Prompt

Use your existing Project 1 solution as the basis for a controlled AI comparison.

Do not provide the AI with your completed source code yet. Instead, describe the problem you previously solved and investigate the solution it produces from that description.

 
Instructions

    Choose one contained part of Project 1 that you have already implemented.
        This may be the Account hierarchy.
        This may be the relationship between Account and Transaction.
        This may be the Client and account relationship.
        Choose an area large enough to contain several design decisions.
    Write a simple prompt asking an AI system to implement the same functionality.
    Include the basic functional requirements but keep the first prompt relatively general.
    Generate a response.
    Keep the generated response separate from your assessed project.
    Do not copy the generated implementation into Project 1.

 
Notes

    The purpose of the first prompt is to establish a baseline.
    You already have your own solution, so the generated code can be evaluated against decisions you have made independently.
    As a privacy notice, please do not provide personal information, credentials, private data, or information unrelated to the programming problem.

 
Task 3: Evaluate the Baseline Response

Compare the generated solution with your existing implementation.

 
Instructions

    Identify similarities between the two solutions.
        Compare the classes created.
        Compare attributes.
        Compare methods.
        Compare relationships.
        Compare inheritance.
        Compare validation and encapsulation.
    Identify differences between the two solutions.
    For each important difference, consider why it occurred.
        Was information missing from the prompt?
        Did the AI make an assumption?
        Did it choose a different but valid design?
        Did it use a concept that has not been taught?
        Did it misunderstand part of the problem?
        Did it introduce unnecessary complexity?
    Identify anything in the generated solution that would not meet the requirements of this course.
    Decide which solution is stronger for the selected problem.
        Your solution may be stronger.
        The generated solution may contain a useful design decision.
        Different parts of each solution may be stronger.
    Justify the comparison using OOP concepts rather than personal preference.

 
Notes

    Different code does not automatically mean incorrect code.
    Generated code should be evaluated against requirements, design principles, and expected behaviour.
    Code that looks more sophisticated is not necessarily a better solution.

 
Task 4: Improve the Prompt

Rewrite the original prompt so that it communicates the programming problem more precisely.

 
Instructions

    Review the differences identified in Task 3.
    Identify information that would have helped the AI produce a more appropriate solution.
    Rewrite the prompt using the following structure.
        Context: Describe what the system represents.
        Goal: State what needs to be implemented.
        Existing Design: Describe classes or relationships that must be preserved.
        Requirements: State the required attributes, methods, relationships, and behaviour.
        Constraints: State important restrictions on the solution.
        Output: State what you want the AI to provide.
    Include relevant course constraints where appropriate.
        Use Python.
        Use object-oriented programming.
        Preserve the specified class structure.
        Use private or protected visibility appropriately.
        Use getters and property() where required.
        Do not introduce concepts that are unnecessary for the problem.
    Generate a second response using the revised prompt.
    Keep this response separate from the assessed Project 1 implementation.

 
Notes

    A longer prompt is not automatically a better prompt.
    Useful prompts provide relevant constraints and remove ambiguity.
    Avoid specifying every line of the solution. The goal is clear communication, not writing the code indirectly through the prompt.

 
Task 5: Compare the Two AI Responses

Investigate what changed when the prompt became more precise.

 
Instructions

    Compare the first and second generated solutions.
    Identify changes caused by the revised prompt.
        Class structure.
        Attribute visibility.
        Relationships.
        Method responsibilities.
        Inheritance.
        Validation.
        Naming.
        Complexity.
    Identify requirements followed more accurately in the second response.
    Identify any problems that remain.
    Consider whether the second response became overly constrained.
        Did the prompt remove useful design decisions?
        Did it effectively describe the solution rather than the problem?
        Did unnecessary constraints make the generated code more complicated?
    Decide whether the improved prompt produced a better response and justify your conclusion.

 
Notes

    Prompt quality can improve an AI response, but a detailed prompt does not guarantee a correct solution.
    Generated outputs still require verification.

 
Task 6: Verify Before You Trust

Perform a final review of one generated solution as if it had been provided during a professional code review.

 
Instructions

    Read the generated code without assuming it is correct.
    Check whether it satisfies the requirements provided in the prompt.
    Check whether the code would run as written.
    Look for assumptions that were not requested.
    Look for missing requirements.
    Look for unnecessary classes, methods, validation, or complexity.
    Identify any concepts you could not confidently explain yourself.
    Select one generated design decision and think about the results. Discuss with your peers:
        What does it do?
        Why might the AI have chosen it?
        Is it appropriate for this project?
        Would you keep, change, or remove it?
        Why?

 
Notes

    Generated code should never be trusted simply because it looks convincing.
    If you cannot explain how generated code works, you cannot reliably verify that it is appropriate.
    Verification is part of using AI responsibly.

# 6-2
Portfolio Exercise
Project 2: Multiple Inheritance
Problem Statement

Project 2 already contains different undead specialisations. WarriorUndead represents undead that rely on martial combat, while CursedUndead represents undead that use supernatural abilities.

A DeathKnight combines both of these characteristics. In this workshop, extend the existing inheritance hierarchy so DeathKnight inherits from both classes. This creates a diamond-shaped inheritance structure through Undead and provides an opportunity to investigate ambiguity, explicit parent-class method calls, and Python's Method Resolution Order.

 
Task 1: Extend the Project 2 Model

Update the existing Project 2 UML class diagram before modifying the implementation.

 
Instructions

    Add DeathKnight to the existing summon hierarchy.
        Make DeathKnight inherit from WarriorUndead.
        Make DeathKnight also inherit from CursedUndead.
    Identify the resulting diamond structure.
        Both inheritance branches lead back to Undead.
    Add specialised Death Knight statistics.
        Minimum health.
        Maximum health.
        Minimum power.
        Maximum power.
        Health gained per level.
        Power gained per level.
        Starting health.
        Starting power.
    Add combat_style() to both intermediate parent classes.
        Include the method in WarriorUndead.
        Include the same method name in CursedUndead.
    Add the new Death Knight behaviours to the model.
        combat_style().
        compare_combat_styles().
    Retain the existing Project 2 relationships.
        Necromancer and its resources.
        Controlled undead.
        Summoning rituals.
        Existing summon types.

 
Notes

    The existing hierarchy should be extended rather than redesigned.
    DeathKnight is the only new summon required in this workshop.
    The same combat_style() method name in both parent classes deliberately creates ambiguity.

 
Task 2: Implement the DeathKnight

Create the new specialised summon and extend the existing parent classes where required.

 
Instructions

    Add combat_style() to WarriorUndead.
        Return information describing direct martial combat.
    Add combat_style() to CursedUndead.
        Return information describing cursed or supernatural combat.
    Create DeathKnight.
        Inherit from WarriorUndead and CursedUndead in the order shown in the UML model.
    Add the specialised stat constants.
        Give the Death Knight higher starting statistics than the earlier summons.
        Give it its own minimum and maximum stat boundaries.
        Give it its own levelling growth values.
    Implement the constructor.
        Accept a unit identifier.
        Use super() to pass the identifier, name, starting health, and starting power through the inheritance hierarchy.
        Do not recreate inherited attributes.
    Confirm the multiple-inheritance relationships using isinstance().
        A DeathKnight should be a WarriorUndead.
        A DeathKnight should be a CursedUndead.
        A DeathKnight should also be an Undead.

 
Notes

    Both parent constructors already use super(), allowing Python to follow the MRO through the complete hierarchy.
    Existing levelling and property behaviour continues to come from Undead.

 
Task 3: Investigate Ambiguity and the MRO

Both parents now provide combat_style(). Determine how Python resolves the ambiguity.

 
Instructions

    Override combat_style() in DeathKnight.
    Call super().combat_style().
        Allow Python to select the next implementation according to the MRO.
    Display the DeathKnight Method Resolution Order.
    Compare the MRO with the result of combat_style().
        Identify which parent implementation was selected first.
    Implement compare_combat_styles().
    Explicitly call both parent implementations.
        Call WarriorUndead.combat_style(self).
        Call CursedUndead.combat_style(self).
    Compare the two approaches.
        super() follows the MRO.
        An explicit class method call selects a particular parent implementation.

 
Notes

    The order of the parent classes in the DeathKnight declaration affects the MRO.
    The shared Undead ancestor occurs only once in the final resolution order.
    Explicit parent-class calls are useful here because the purpose is to deliberately compare both implementations.

 
Task 4: Integrate and Demonstrate the Death Knight

Connect the new summon to the existing Project 2 system.

 
Instructions

    Create a new SummoningRitual for DeathKnight.
    Give the ritual a higher resource cost than the earlier summons.
        Require Necrotic Runes.
        Require Spirit Runes.
        Require Bone Runes.
        Require Flesh Runes.
        Require Ectoplasm.
    Summon the Death Knight through the existing Necromancer.
        Do not instantiate it directly as part of the normal summoning process.
    Demonstrate the new inheritance structure.
        Display the Death Knight.
        Complete the isinstance() checks.
        Display the MRO.
    Demonstrate ambiguous behaviour.
        Call combat_style().
        Observe the implementation selected through super().
    Demonstrate explicit class method calls.
        Call compare_combat_styles().
        Confirm that both parent implementations can be selected directly.
    Confirm that existing inherited behaviour still works.
        Command the Death Knight through the necromancer.
        Level the Death Knight.
        Display its updated statistics.
    Compare the finished implementation with the updated UML model.
        Confirm the multiple-inheritance relationships.
        Confirm the diamond structure.
        Confirm method placement.
        Correct any differences between the model and implementation.

 
Notes

    The existing Necromancer, ResourcePool, and SummoningRitual responsibilities should remain unchanged.
    This task extends the existing design rather than replacing it.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

 
# 7-1
Portfolio Exercise
Problem Statement

Project 3 is your Creative Piece: an object-oriented program based on a domain you are interested in. You will design and incrementally develop a solution that applies the concepts learned throughout the course, including classes, relationships, encapsulation, inheritance, polymorphism and abstraction where they meaningfully support the design.

Choose a domain you understand or enjoy, such as a game, sport, hobby, collection or other interest. The goal is to create a coherent object-oriented program that demonstrates your ability to model a problem, justify your design choices and extend the program as new concepts are introduced.

 
Task 1: Finalise Project 2

Project 2 reaches its conclusion in this workshop. Take a short amount of time to clean up the Necromancy project and leave it in a complete, understandable state.

 
Instructions

    Review the current Project 2 implementation.
        Confirm the code matches your latest model.
        Confirm the inheritance hierarchy is represented correctly.
        Confirm the Death Knight multiple-inheritance structure operates as intended.
        Confirm summoning, resources, levelling and commands still work after the later changes.
    Run the complete Project 2 demonstration.
        Create several different summons.
        Include the Death Knight.
        Demonstrate the important relationships and behaviours developed throughout the project.
    Tidy the project before leaving it.
        Remove temporary testing code that is no longer useful.
        Correct obvious naming, formatting or organisation problems.
        Leave the project in a state that clearly demonstrates the concepts you implemented.

Notes

Project 2 is complete after this task. You do not need to redesign or substantially extend it.
Project 3: Creative Piece
Task 2: Choose Your Creative Piece

Project 3 gives you more freedom to choose what you want to model. Start with a domain you already enjoy or understand so that you can spend more time thinking about the object-oriented design rather than learning an unfamiliar subject.

 
Instructions

    Choose a domain for your Creative Piece.
        A game you play.
        A sport you follow.
        A hobby or collection.
        Music, film or television.
        Cooking or food.
        Vehicles.
        Technology.
        Something else you are interested in.
    Decide what part of that domain you want to model.
        Keep the scope manageable.
        Choose something with several related objects and meaningful behaviours.
    Write a short description of your idea.
        Explain what the program represents.
        Identify what the program will allow its objects to do.
    Discuss your idea with a tutor if you are unsure what to create.
        Bring your interests or hobbies to the discussion.
        A tutor can help turn an idea into an appropriate object-oriented program.

 
Notes

Choose something you actually find interesting. A familiar domain usually makes it easier to identify realistic objects, attributes, behaviours and relationships. Something you know well will help you with taking on this project. Be creative! :D

 
Task 3: Begin the Object Model

Before implementing the Creative Piece, identify the main objects and how they relate to one another.

 
Instructions

    Identify several classes that belong in your Creative Piece.
    For each class, identify:
        Important attributes.
        Important behaviours.
        Which information belongs inside that class.
    Identify relationships between the classes.
        Association.
        Aggregation.
        Composition.
        Inheritance where a genuine generalisation and specialisation relationship exists.
    Begin a UML class diagram for the Creative Piece.
    Review the model before implementing it.
        Look for classes with too many unrelated responsibilities.
        Look for duplicated attributes or behaviours.
        Look for relationships that could make the design clearer.

 
Notes

Use the modelling skills developed earlier in the course. The model does not need to be final yet. Project 3 will continue to evolve as new concepts are introduced. I always find working on the code and model together helps me identify what I need to implement and how. The what comes from the diagram, and as I code, I understand how it all connects, and then update my diagram.

 
Task 4: Build the Foundation

Implement the first working version of the Creative Piece using the object-oriented practices developed throughout the course.

 
Instructions

    Create the classes from your initial model.
    Implement constructors and create several objects.
    Encapsulate object data appropriately.
    Add getters, setters or properties where information genuinely needs to be accessed or changed.
    Add meaningful object methods.
        Give objects behaviours that belong to their responsibilities.
        Avoid creating classes that only store values.
    Separate classes into appropriate modules.
    Add useful string conversions so important objects can be inspected during the demonstration.
    Create a small main.py demonstration showing the first version working.

 
Task 5: Apply the Concepts You Have Learned

Review the concepts from earlier topics and identify where they can strengthen the Creative Piece.

 
Instructions

    Review your design for opportunities to use:
        Object relationships.
        Composition or aggregation.
        Constants.
        Helper methods.
        Equality where objects need meaningful comparison.
        Inheritance.
        Method overriding.
        super().
        Protected attributes within an inheritance hierarchy.
    Consider whether multiple inheritance has a genuine use in your domain.
        Use it where one object meaningfully combines responsibilities from multiple parent classes.
        Review the MRO when multiple inheritance is used.
    Consider whether part of the design represents a broader concept that should not be created directly.
        Introduce an abstract class where appropriate.
    Look for behaviour that several different object types can perform through a common interface.
        Use polymorphism instead of repeatedly checking concrete object types.
    Update the UML model as the implementation changes.

 
Notes

Do not add a concept simply because it has appeared in the course. Use the concepts that improve the design and be able to explain why they belong there.

 
Task 6: Create an Initial Creative Piece Demonstration

Your Creative Piece is still in development, but it now needs a demonstration that proves the current object model works together.

 
Instructions

    Create multiple objects from the classes you have implemented.
    Demonstrate interactions between related objects.
    Demonstrate at least one inheritance hierarchy where it forms part of your design.
    Demonstrate overridden or polymorphic behaviour where applicable.
    Include an abstract class or interface-style design where it suits your model.
    Run the program from main.py and confirm that the current implementation behaves consistently with your UML model.
    Record areas you want to extend in later workshops.

 
Task 7: Record Your Weekly Code Review

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 7-2
Portfolio Exercise
Project 1: Finance
Problem Statement

Project 1 already contains an Account inheritance hierarchy with SavingsAccount and EverydayAccount. In this workshop, you will refine that hierarchy using abstraction and demonstrate how the specialised account types can be used polymorphically through their shared parent design.

 
Task 1: Make Account Abstract

Refine the existing Account hierarchy so that Account represents the shared idea of an account without being created directly.

 
Instructions

    Update Account to inherit from ABC.
    Identify behaviour that every specialised Account must provide.
        Use abstractmethod to require this behaviour from subclasses.
        Keep behaviour shared by every account in the parent class.
    Update SavingsAccount and EverydayAccount to satisfy the abstract requirements.
        Preserve their existing specialised withdrawal rules.
        Continue using inherited behaviour where it already belongs in Account.
    Attempt to create an Account object directly.
        Observe how Python prevents an incomplete abstract class from being instantiated.

 
Task 2: Demonstrate Account Polymorphism

Use the shared Account abstraction to work with different specialised accounts through the same operations.

 
Instructions

    Create at least one SavingsAccount and one EverydayAccount.
    Give each account enough balance to demonstrate a withdrawal.
    Call the same withdrawal behaviour on both account types.
    Demonstrate that each object follows its own specialised withdrawal rules.
    Use the shared Account behaviour without checking whether an object is specifically a SavingsAccount or EverydayAccount.
    Demonstrate other inherited behaviour, such as deposits, transaction recording or string conversion, where it supports the example.

 
Task 3: Update the Project 1 Model and Demonstration

Bring the model and demonstration up to date with the abstraction added in this workshop.

 
Instructions

    Update the UML model.
        Mark Account as abstract.
        Show any abstract behaviour.
        Confirm the generalisation relationships to SavingsAccount and EverydayAccount.
    Review main.py.
        Remove any direct creation of Account.
        Demonstrate both specialised account types.
        Include a clear example of polymorphic behaviour.
    Run the Project 1 demonstration and confirm the existing Client, Account and Transaction relationships still operate correctly.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 8-1
Portfolio Exercise
Project 3: Creative Piece

Continue developing your Creative Piece by introducing two data structures that meaningfully support the objects and behaviours in your design. Choose from Lists, Sets, and Dictionaries. They must be used how we are teaching them in the course, i.e., if you choose lists, I suggest implementing comprehension at a minimum and a good use case for filtering. Ensure they are used meaningfully, do not choose a set or dictionary unless it applies to your project. 

 
Task 1: Choose Your Data Structures

Review your Creative Piece and identify two places where a data structure can improve how information is stored or managed.

 
Instructions

    Choose two of the following data structures:
        List.
        Set.
        Dictionary.
    Identify what each structure will store in your Creative Piece.
    Match the structure to the kind of data you need to manage.
        Use a List where order or repeated values are meaningful.
        Use a Set where values need to remain unique.
        Use a Dictionary where values need to be accessed through meaningful keys.
    Record a short explanation of why each structure suits its purpose.

 
Task 2: Implement the Data Structures

Add both selected data structures to the existing object model and use them as part of meaningful class behaviour.

 
Instructions

    Add the first data structure to the class where that collection belongs.
        Populate it through object behaviour.
        Add methods that use or modify the stored data.
    Add the second data structure to another suitable part of the design.
        Use it for a different purpose from the first structure.
        Add behaviour that demonstrates why this structure was selected.
    Maintain encapsulation around the stored collections.
        Provide controlled access where the data needs to be viewed externally.
    Continue using objects inside the structures where this suits the design.

 
Task 3: Extend the Creative Piece

Use the new collections to add a small amount of useful behaviour to the Creative Piece.

 
Instructions

    Add operations that work with the contents of the two data structures.
    Include behaviour such as:
        Adding and removing objects.
        Looking up information.
        Checking membership.
        Finding related objects.
        Combining or comparing collections.
        Calculating information from stored objects.
    Keep the behaviour connected to the domain of your Creative Piece.
    Update the UML model where the new collections affect attributes or relationships.

 
Task 4: Demonstrate the Data Structures

Update the Creative Piece demonstration so that the purpose of both selected data structures can be seen clearly.

 
Instructions

    Create enough objects to meaningfully populate both structures.
    Demonstrate adding information to each structure.
    Demonstrate at least one operation that makes use of the characteristics of each selected structure.
    Display useful results from the operations.
    Confirm that the behaviour matches the current UML model and Creative Piece design.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 8-2
Portfolio Exercise
Project 1: Finance

Project 1 already contains collections of related objects, particularly Accounts belonging to a Client and Transactions belonging to an Account. In this workshop, you will refine these areas using data structures that better match how the information is accessed and managed.

 
Task 1: Store Client Accounts in a Dictionary

A Client needs to manage multiple Account objects and retrieve a specific account efficiently. A Dictionary is suitable because each Account already has a unique account number that can be used as a key.

 
Instructions

    Update the Client class so its Accounts are stored in a Dictionary.
        Use the account number as the key.
        Store the corresponding Account object as the value.
    Update the behaviour used to add an Account.
        Accept valid Account objects.
        Store each Account using its account number.
    Add behaviour to retrieve a specific Account by account number.
    Add behaviour to remove an Account using its account number where this fits the current design.
    Provide controlled access to the Account collection.
        Prevent external code from directly modifying the internal Dictionary.
    Update any existing Client behaviour that previously relied on a different way of storing Accounts.

 
Task 2: Manage Transactions with a List

Each Account can contain many Transaction objects over time. A List is suitable because transactions form an ordered history where multiple transactions can contain similar values.

 
Instructions

    Review how Transaction objects are currently stored inside Account.
    Store the Account's Transaction history in a List.
    Ensure deposit and withdrawal behaviour continues to create and record Transaction objects.
    Add behaviour that can return the transaction history without exposing the internal List directly.
    Add at least one useful operation that processes the transaction history.
        Retrieve transactions of a particular type.
        Calculate the number of transactions.
        Find transactions above a given amount.
        Display the transaction history.
    Keep the Transaction objects in the order they were recorded.

 
Task 3: Use the Structures Through Existing Behaviour

Update the Finance project so the new data structures form part of the existing object interactions rather than remaining isolated collections.

 
Instructions

    Create a Client with multiple specialised Account objects.
    Retrieve an Account through the Client using its account number.
    Perform several deposits and withdrawals on the retrieved Account.
    Access the Account's transaction history.
    Demonstrate at least one operation that processes the stored Transaction objects.
    Confirm that SavingsAccount and EverydayAccount continue to follow their specialised behaviour while using the same collection structures.

 
Task 4: Update the Project Model

Keep the Project 1 model aligned with the implementation changes made in this workshop.

 
Instructions

    Update the UML model to represent the Account collection managed by Client.
    Show the multiplicity between Client and Account.
    Update the Account and Transaction relationship where required.
    Include collection attributes where they are useful for understanding the model.
    Check that the abstract Account hierarchy from Topic 7 remains represented correctly.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 9-1
Portfolio Exercise
Project 3: Creative Piece

Project 3 now needs a complete automated test suite. You will use pytest to test the behaviour of every testable class in the Creative Piece, use fixtures to prepare reusable test objects, and use code coverage to identify parts of the implementation that have not yet been exercised.

 
Task 1: Identify What Needs Testing

Review the current Creative Piece and identify the behaviours that can be tested through predictable inputs and outcomes.

 
Instructions

    Review every class currently implemented in Project 3.
    Identify the testable behaviour in each class.
        Constructors and resulting object state where relevant.
        Methods that calculate or return values.
        Methods that change object state.
        Collection behaviour.
        Relationships between objects.
        Overridden and polymorphic behaviour.
        Validation and boundary conditions.
    Identify important valid and invalid scenarios for each behaviour.
    Plan enough tests to cover the meaningful behaviour of every testable class.

 
Notes

Do not create tests for getters and setters. Test the behaviour that uses and changes the object's data. If you notice a getter or setter never being used. I recommend removing it.

 
Task 2: Create the Pytest Test Suite

Create a structured pytest test suite for the Creative Piece.

 
Instructions

    Create test modules for the classes in Project 3.
        Use pytest naming conventions so the tests are discovered automatically.
        Group related tests together logically.
    Write tests for each testable class.
    Include tests for:
        Expected successful behaviour.
        Important alternative outcomes.
        Boundary conditions.
        Invalid operations where the class handles them.
        State changes caused by methods.
    Use assertions to verify the actual result of each operation.
    Use pytest.approx() where calculations involve floating-point values.
    Run the complete suite regularly as tests are added.

 
Task 3: Create and Use Fixtures

Many tests require objects to begin in the same known state. Use pytest fixtures to reduce repeated setup and keep the tests easier to understand.

 
Instructions

    Identify objects or groups of objects that are created repeatedly across the test suite.
    Create fixtures for useful reusable test data.
    Use fixtures to provide:
        Common individual objects.
        Objects containing existing data.
        Related objects required for interaction tests.
    Use the fixture parameters directly in the tests that require them.
    Keep fixtures focused on setup.
        Perform the behaviour being tested inside the test itself.

 
Task 4: Test Object Interactions

Project 3 contains relationships between objects, so the test suite also needs to verify that these objects work together correctly.

 
Instructions

    Test important relationships in the Creative Piece.
    Verify behaviour involving collections of objects.
    Test inherited and overridden behaviour through concrete classes.
    Test polymorphic behaviour where multiple object types can be used through the same abstraction.
    Test operations that involve more than one object when those interactions are an important part of the Creative Piece.
    Confirm that failed operations leave objects in an appropriate state where relevant.

 
Task 5: Measure Code Coverage

Use code coverage to identify areas of the Creative Piece that the current test suite does not exercise.

 
Instructions

    Run the complete test suite with code coverage enabled.
    Review the coverage report for each Project 3 module.
    Identify:
        Classes that have not been tested.
        Methods that have not been exercised.
        Branches of behaviour that the current tests do not reach.
    Add meaningful tests for important uncovered behaviour.
    Repeat the coverage process as the test suite develops.
    Reach the high level of code coverage expected by the Project 3 rubric across the testable implementation.

 
Notes

Coverage is evidence that code has been executed by the test suite. High coverage still needs meaningful assertions that verify the behaviour being exercised.

 
Task 6: Run the Complete Test Suite

Finish with a complete run of the Project 3 tests and resolve any failures.

 
Instructions

    Run the entire pytest suite together.
    Investigate every failing test.
        Determine whether the problem is in the implementation or the test.
        Correct the appropriate code.
    Run the suite again after each correction.
    Confirm that:
        All testable classes are represented in the suite.
        Fixtures are used where repeated setup exists.
        All tests pass.
        Code coverage meets the expected standard.
        The Creative Piece still behaves correctly through its normal demonstration.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 9-2
Portfolio Exercise
Project 1: Finance

Project 1 now needs a complete automated test suite. Use pytest to test the behaviour of the Finance classes, use fixtures for repeated setup, and use code coverage to identify important behaviour that has not yet been exercised.

 
Task 1: Identify Testable Behaviour

Review Project 1 and identify the behaviours that need automated testing.

 
Instructions

    Review the current Finance classes.
        Client.
        Account.
        SavingsAccount.
        EverydayAccount.
        Transaction.
        Any other classes still used by the current design.
    Identify testable behaviour in each concrete class.
        Deposits and withdrawals.
        Specialised withdrawal rules.
        Transaction creation and storage.
        Account storage and retrieval through Client.
        Collection behaviour.
        Validation and important boundary conditions.
        Inherited and overridden behaviour.
    Plan tests for both successful and unsuccessful operations.
    Do not create tests simply for getters and setters. (See 9-1 for more info)

 
Task 2: Create the Project 1 Test Suite

Create pytest tests that cover the meaningful behaviour of the Finance project.

 
Instructions

    Create test modules for the testable classes.
    Follow pytest naming conventions so the suite can be discovered automatically.
    Test the shared Account behaviour through concrete Account types.
    Test SavingsAccount.
        Confirm valid withdrawals.
        Confirm the minimum balance rule is enforced.
        Confirm failed withdrawals leave the balance unchanged.
    Test EverydayAccount.
        Confirm valid withdrawals.
        Confirm the maximum withdrawal rule is enforced.
        Confirm failed withdrawals leave the balance unchanged.
    Test Transaction behaviour where it produces meaningful outcomes.
    Test Client behaviour.
        Add multiple Account objects.
        Retrieve Accounts using their account numbers.
        Confirm the Account dictionary behaves correctly.
    Use clear assertions to verify each expected result.

 
Task 3: Use Pytest Fixtures

Create reusable setup for Finance objects that are needed across multiple tests.

 
Instructions

    Identify objects that are repeatedly created throughout the suite.
    Create fixtures for useful Finance objects.
        A SavingsAccount with a known balance.
        An EverydayAccount with a known balance.
        A Client containing several Accounts.
        Other repeated object combinations used by multiple tests.
    Pass fixtures into the tests that require them.
    Keep the fixture focused on preparing the starting state.
    Perform the behaviour being tested inside the test itself.

 
Task 4: Test Finance Object Interactions

Test the relationships between the Finance classes rather than only testing each class in isolation.

 
Instructions

    Test that deposits and withdrawals create Transaction objects where required.
    Confirm Transaction objects are stored in the Account's transaction history.
    Test that multiple Transaction objects remain in the expected order.
    Retrieve an Account through a Client and perform operations on the returned object.
    Confirm that both SavingsAccount and EverydayAccount can be managed through the same Client behaviour.
    Test polymorphic Account behaviour without checking concrete Account types inside the test scenario.

 
Task 5: Measure and Improve Code Coverage

Run the Project 1 suite with code coverage and use the results to find gaps in the tests.

 
Instructions

    Run the complete pytest suite with code coverage enabled.
    Review the coverage report for the Finance modules.
    Identify important methods or branches that have not been exercised.
    Add meaningful tests for uncovered behaviour.
    Run the suite and coverage report again.
    Continue until Project 1 reaches the high level of coverage expected by the rubric across its testable implementation.

 
Notes

High coverage is useful when the tests also contain meaningful assertions. Executing a line of code does not automatically prove that its behaviour is correct.

 
Task 6: Run the Complete Finance Test Suite

Finish by running all Project 1 tests together and resolving any remaining failures.

 
Instructions

    Run the complete pytest suite.
    Investigate every failing test.
        Determine whether the implementation or the test needs correction.
    Confirm that:
        All testable Finance classes are represented.
        Fixtures are used where setup is repeated.
        Important valid and invalid behaviours are tested.
        Object interactions are included.
        All tests pass.
        Code coverage meets the expected standard.
    Run the normal Project 1 demonstration again to confirm the Finance program still behaves correctly.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 10-1
Portfolio Exercise
Project 3: Creative Piece

Project 3 now needs to respond appropriately when an operation cannot be completed. Add exception handling to situations that are meaningful within your Creative Piece, rather than using exceptions simply because the concept has been introduced. Please ensure you always catch exceptions which are raised, and not in your main.py module. 

 
Task 1: Identify Exceptional Situations

Review the Creative Piece and identify operations where something can go wrong and the program needs to respond.

 
Instructions

    Identify several meaningful invalid operations in your project.
        An object does not exist.
        An action cannot occur in the object's current state.
        A supplied value breaks an important rule.
        An object cannot participate in the requested operation.
    Choose situations where an exception communicates the problem more clearly than normal program flow.
    Record what causes each exception and what information is useful when it occurs.

 
Task 2: Create Custom Exceptions

Create exceptions that represent problems specific to the domain of your Creative Piece.

 
Instructions

    Create custom exception classes for the situations identified in Task 1.
    Give each exception a name that clearly communicates the problem it represents.
    Inherit from Exception or create a shared parent exception where several errors belong to the same category.
    Include useful information in the exception message.
        Keep the message relevant to the domain.
        Include values or object information where this helps explain the failure.

 
Task 3: Raise Exceptions

Integrate the custom exceptions into the existing Project 3 behaviour.

 
Instructions

    Locate the methods responsible for enforcing each rule.
    Use raise when an invalid condition is detected.
    Raise the custom exception that best represents the problem.
    Raise the exception before making changes that would leave an object in an invalid state.
    Continue using normal return values for ordinary successful behaviour.

 
Task 4: Handle Exceptions

Use try and except where the program needs to recover from an exceptional operation.

 
Instructions

    Add exception handling around operations that can raise the custom exceptions.
    Handle the expected exception and provide useful feedback.
    Keep exception handling within the object-oriented behaviour of the project rather than placing the handling in main.py.
    Confirm that a failed operation does not corrupt the state of the objects involved.
    Confirm that the program can continue after a handled exception.

 
Task 5: Test Raised Exceptions

Extend the existing pytest suite to verify exception behaviour.

 
Instructions

    Identify methods where a custom exception can be observed directly by the test suite.
    Use pytest.raises() to confirm that the expected custom exception is raised.
    Test the condition that causes the exception.
        Use realistic objects and values from the Creative Piece.
    Check exception information where it forms an important part of the behaviour.
    Continue testing the resulting object state where failed operations must leave data unchanged.

 
Notes

pytest.raises() verifies that an exception is part of the expected behaviour rather than an unexpected test failure. i.e., be careful where you test this. 

 
Task 6: Demonstrate the Updated Creative Piece

Update the Project 3 demonstration to show how exception handling fits into the existing program.

 
Instructions

    Demonstrate normal successful behaviour.
    Trigger several of the new exceptional situations.
    Show the feedback produced when an exception is handled.
    Continue using the program after a handled exception.
    Confirm that the existing abstraction, inheritance, data structures and other Project 3 behaviour still operate correctly.

 
Task 8: Finalise Project 3

Project 3 is now close to submission. Use this task to review the complete Creative Piece against the assessment requirements and make any final corrections before submission.

 
Instructions

    Read through the Project 3 rubric carefully.
        Check each criterion against the current implementation.
        Confirm that the required object-oriented concepts are demonstrated clearly.
        Identify any criterion that is not yet supported by the submitted code or documentation.
    Review the complete project.
        Confirm the UML model matches the final implementation.
        Confirm the main demonstration shows the important behaviour of the Creative Piece.
        Confirm the pytest suite passes.
        Confirm code coverage meets the expected standard.
        Confirm exception handling works as intended.
    Review code quality.
        Check naming and formatting.
        Remove temporary or redundant testing code.
        Remove unused classes, methods or imports.
        Confirm responsibilities remain appropriately separated between classes.
    Check the project as a complete submission.
        Confirm all required files are included.
        Confirm the program runs from the expected entry point.
        Confirm the project can be understood without relying on unfinished notes or temporary development code.
    Make final changes based on the rubric and any tutor feedback received during the project.

 
Notes

Use the rubric as the final checklist!!!

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.

# 10-2
Portfolio Exercise
Project 1: Finance

Project 1 now reaches its final stage. Add exception handling to meaningful Finance operations, extend the existing pytest suite to verify the new behaviour, and complete a final review of the project before submission.

 
Task 1: Identify Finance Exceptions

Review the Finance project and identify situations where an operation cannot be completed because an important Finance rule has been broken.

 
Instructions

    Identify several meaningful exceptional situations in the current design.
        An Account cannot complete a withdrawal.
        A Savings Account would fall below its minimum balance.
        An Everyday Account exceeds its maximum withdrawal amount.
        An Account number cannot be found for a Client.
        Another existing Finance rule is violated.
    Decide which situations are suitable for custom exceptions.
    Record what causes each exception and what information needs to be communicated when it occurs.

 
Task 2: Create Custom Finance Exceptions

Create custom exceptions that represent problems specific to Project 1.

 
Instructions

    Create appropriately named custom exception classes for the situations identified in Task 1.
    Inherit from Exception, or introduce a shared Finance exception parent where several exceptions belong together.
    Provide useful exception messages.
        Include relevant Account information.
        Include amounts, limits or balances where they help explain the problem.
    Keep the exceptions connected to meaningful Finance rules already present in the project.

 
Task 3: Raise and Handle Exceptions

Integrate the new exceptions into the existing Finance behaviour.

 
Instructions

    Locate the methods responsible for enforcing each Finance rule.
    Use raise when an exceptional condition is detected.
    Use try and except to handle expected exceptions where the program needs to recover.
    Ensure exceptions are raised before an invalid operation changes the object's state.
    Confirm failed operations leave Account balances, Transaction histories and other related data unchanged.
    Keep exception handling within the Finance classes rather than placing try / except behaviour in main.py.

 
Task 4: Extend the Project 1 Test Suite (Optional)

Update the existing pytest suite so the new exception behaviour is tested alongside the Finance behaviour completed in Topic 9.

 
Instructions

    Add tests for the new exceptional situations.
    Use pytest.raises() where an exception is expected to propagate from the behaviour being tested.
    Verify important information contained in the raised exception where relevant.
    Confirm that unsuccessful Finance operations do not incorrectly change:
        Account balances.
        Transaction history.
        Client Account collections.
    Run the complete Project 1 test suite after adding the exception tests.
    Check code coverage again and confirm the new exception paths are represented.

 
Task 5: Update the Finance Demonstration

Update the existing Project 1 demonstration so the final Finance project shows both successful and unsuccessful operations.

 
Instructions

    Demonstrate normal Account behaviour.
    Include examples that trigger the new Finance exceptions.
    Show that the program continues after an expected exception has been handled.
    Demonstrate both SavingsAccount and EverydayAccount.
    Include Client, Account and Transaction interactions where they form part of the final design.
    Confirm the demonstration matches the current UML model.

 
Task 6: Finalise Project 1

Project 1 is now ready for its final review. Check the complete Finance project against the assessment requirements and resolve any remaining issues before submission.

 
Instructions

    Read through the Project 1 rubric carefully.
        Check every criterion against the current implementation.
        Confirm the required object-oriented concepts are clearly demonstrated.
        Identify anything that is incomplete or not clearly evidenced.
    Review the complete implementation.
        Confirm the UML model matches the final code.
        Confirm the demonstration represents the important Finance behaviour.
        Confirm the pytest suite passes.
        Confirm code coverage meets the expected standard.
        Confirm exception handling behaves correctly.
    Review code quality.
        Check naming and formatting.
        Remove temporary development code.
        Remove unused imports or obsolete behaviour.
        Confirm responsibilities remain appropriately separated between classes.
    Confirm the final project contains all required submission material.
    Make any final changes based on the rubric and tutor feedback.

 
Notes

Use the rubric as the final checklist for Project 1. Focus on clearly demonstrating the completed work rather than adding unnecessary new features.

 
Task: Record Your Weekly Code Review

Complete an in-person code review during one of your two workshops and record the discussion as part of your Programming Portfolio. A code review does not need to be a formal meeting. A short conversation with your workshop supervisor about a class, method, design decision, error, or possible improvement can count as a code review when the discussion is recorded and leads to meaningful reflection or development.

 
Instructions

    Use the code review record in the main folder of your project.
        Either your created README.md file or a clearly named text file such as code_reviews.txt.
    Add a heading for the current workshop.
        Include the workshop number or week.
        Include the date of the review.
        Include the name of the person who reviewed the code with you.
    Briefly record the discussion.
        Identify the class, method, module, diagram, or section of code that was reviewed.
        Summarise the feedback, suggestion, question, or problem discussed.
        Explain why the discussion was relevant to the current stage of the project.
    Record the resulting development.
        Describe at least one change made because of the review.
        Include the relevant code or other evidence where appropriate.
        Explain how the change improved the code or your understanding.
    Retain the review record with the project.
        Update the file after each weekly review.
        Ensure each review has its own heading.

 
Notes

    Casual code discussions are acceptable when they are recorded clearly.
    The review should involve meaningful discussion.
    A brief review is sufficient when it identifies useful feedback and a resulting change.
    Ensure the code review record meets the requirements of the rubric.


# Expectations & Minimum Requirements 

Some Criterion are dependant on a set of minimum requirements. i.e., PEP8 formatting. Here is a list which you may refer to: 

    Two chosen data structures are meaningfully implemented within the program. Data structures included only to demonstrate their existence do not meet this requirement.
    Required PEP8 Includes:
        Indentation - 4 spaces per level.
        Line Length - 79 characters for code and 72 for docstrings.
        Imports - Each on separate lines and avoid wildcard imports.
        Whitespace - Avoid irrelevant whitespace.
        Comments - Complete sentence and used sparingly. Inline comments preceded by at least two spaces.
        Naming Convention - Snake case (lowercase_with_underscores) for function and variable names. Title case (TitleCase) for class names.
        Blank Lines - Surround functions and class definitions with two blank lines. Surround methods with one blank line.
     For clarification, a PEP8 violation refers to a required rule being violated, rather than every individual occurrence of that violation. i.e., You disregard line length several times is counted as 1 violation. Running autopep8 does not ensure compliance with every requirement in the above list. Naming conventions, quality of comments and several documentation requirements still require manual inspection. Therefore including running autopep8 is only an expectation.
    Exceptions are caught and handled within the class responsible for the operation which may raise them. Exception handling placed within the main module does not meet this minimum requirement.
    Integration Testing in main.py is an expectation regardless of it being omitted from the rubric.
    Correctly applies Object-Oriented concepts taught within the course. Only standard libraries may be used appropriately which are not taught in the course.

# Rubrics
Programming Portfolio: Completed
Criteria	Ratings	Points
Criterion 1: Object-Oriented Design & Modelling
	
High Distinction
Demonstrate exceptional object-oriented design, including complete adherence to Object-Oriented principles of abstraction, polymorphism, encapsulation, and SOLID design principles. 

Inheritance, composition, aggregation, and association are meaningfully and accurately applied within the diagrams and programs where appropriate. 

Relationships (Arrows, multiplicity, and labels) are correctly modelled. 

Chosen classes are appropriate for the problem being solved and model the real world.
  
Class diagram accurately represents the implemented classes, data types, attributes, methods, and relationships throughout.
4 pts
Distinction
Demonstrates well-rounded object-oriented design, including complete adherence to Object-Oriented principles of abstraction, polymorphism, encapsulation, and SOLID design principles. 

Inheritance, composition, aggregation, and association are meaningfully and accurately applied within the diagrams and programs where appropriate. 

Arrows, multiplicity, and labels are correctly written. 

Chosen classes are appropriate for the problem being solved and model the real world.

Class diagram closely represents the implemented classes, data types, attributes, methods, and relationships.
3.2 pts
Credit
Demonstrates foundational object-oriented design, including complete adherence to Object-Oriented principles of abstraction, polymorphism, encapsulation, and SOLID design principles. 

Inheritance, composition, aggregation, and association are mechanically applied within the diagrams and programs where appropriate. 

Arrows are correctly written and multiplicity and labels mostly align with the code. 

Chosen classes are appropriate for the problem being solved or to demonstrate a relationship and model the real world.
  
Class diagram mostly represents the implemented classes, data types, attributes, methods, and relationships.
2.8 pts
Pass
Demonstrates foundational object-oriented design, including complete adherence to Object-Oriented principles of abstraction, polymorphism, encapsulation, and SOLID design principles. 

Inheritance, composition, aggregation, and association are mechanically applied within the diagrams and programs where appropriate. 

Arrows are correctly written. 
Multiplicity and labels align with the code for at least one relationship. 

Chosen classes are appropriate for the problem being solved or to demonstrate a relationship and model the real world.

Class diagram represents the core implemented classes, data types, attributes, methods, and relationships.
2 pts
Fail
Not yet able to demonstrate foundational object-oriented design, including complete adherence to Object-Oriented principles of abstraction, polymorphism, encapsulation, and SOLID design principles. 

Not yet able to mechanically apply inheritance, composition, aggregation, or association within the diagrams and programs where appropriate. 

Not yet able to show arrows, multiplicity, and / or labels correctly. 

Not yet able to choose classes which are appropriate for the problem being solved and model the real world.
  
Not yet able to create a class diagram which meaningfully represents the implemented classes, data types, attributes, methods, and relationships.
0 pts
	
/4 pts
Criterion 2: Object-Oriented Implementation & Structure
	
High Distinction
Functionality implementation is logical and correct for what operation is being achieved. 

Specifications surrounding required functionality are completely adhered to. 

File structure demonstrates one class per module and imported as necessary. 

Code contains no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Completely consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed and all parameters are purposeful to the method.
4 pts
Distinction
Functionality implementation is logical and correct for what operation is being achieved. 

Specifications surrounding required functionality are completely adhered to. 

File structure demonstrates one class per module and imported as necessary. 

Code minimal to no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Mostly consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed and all parameters are purposeful to the method.
3.2 pts
Credit
Functionality implementation is logical and correct for what operation is being achieved. 

Specifications surrounding required functionality are mostly adhered to. 

File structure demonstrates one class per module and imported as necessary. 

Code minimal to no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Mostly consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed and all parameters have a use.
2.8 pts
Pass
Functionality implementation is logical and mostly correct for what operation is being achieved. 

Specifications surrounding required functionality are somewhat adhered to. 

File structure demonstrates one class per module and imported as necessary. 

Code minimal to no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Somewhat consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed.
2 pts
Fail
Not yet able to implement functionality which is logical and correct for what operation is being achieved.

Not yet able to adhere to core required functionality. 

Not yet able to structure files indicating one class per module and imported as necessary. 

Not yet able to write exclude extraneous elements, including dead code, redundant code, or hard-coded elements. 

Not yet able to write consistent code and problem-solving approach throughout. 

Not yet able to define methods which describe the operation being performed.
0 pts
	
/4 pts
Criterion 3: Exception Handling & Data Structures
	
High Distinction
All exceptions are caught that might be raised and handled appropriately and effectively.

Exceptions are caught and handled within the classes responsible for the operations which may raise them.

Two chosen data structures are meaningfully and effectively implemented within each project. Lists are correctly implemented in project 2.

Data structures are appropriately selected for the data being stored and the operations being performed.

Operations performed on the data structures demonstrate effective use of their characteristics and purpose.
4 pts
Distinction
Most exceptions are caught that might be raised and handled appropriately.

Exceptions are caught and handled within the classes responsible for the operations which may raise them.

Two chosen data structures are meaningfully implemented within each project. Lists are correctly implemented in project 2.

Data structures are appropriately selected for the data being stored and the operations being performed.

Operations performed on the data structures demonstrate appropriate use of their characteristics and purpose.
3.2 pts
Credit
Exceptions are captured that might be raised and provide an error message.

Exceptions are captured within the classes responsible for the operations which may raise them.

Two chosen data structures are meaningfully implemented within each project. Lists are correctly implemented in project 2.

Data structures are mostly appropriate for the data being stored and the operations being performed.

Data structures are used to perform meaningful operations within the program.
2.8 pts
Pass
Exceptions are captured within the classes responsible for the operations which may raise them.

Two chosen data structures are meaningfully implemented within each project. Lists are correctly implemented in project 2.

Data structures are used to store, access, or manipulate data meaningfully within the program.
2 pts
Fail
Not yet able to capture exceptions.

Not yet able to place handled exceptions outside of the main module or are not meaningfully implemented.

Not yet able to meaningfully implement two chosen data structures within each project or not yet able to correclt implement lists in project 2.


Not yet able to mechanically include data structures with meaningful use, or not yet able to appropriately support the data being stored or manipulated.
0 pts
	
/4 pts
Criterion 4: Documentation & Professional Practice
	
High Distinction
Formatted to the required PEP8 guidelines with no violations (including running autopep8 with default settings). 

Comments accurately convey the purpose and / or meaning of the code block within the overall program.

Code is lightly commented without restating the code.

Complex logic, long code, or design-specific code is clearly and thoroughly explained. 

Comments are clear, full sentences beginning with a capital letter and ending in a full stop.

A class docstring is written for each class for at least 1 project.
4 pts
Distinction
Formatted to the required PEP8 guidelines with one violation of any given rule. (including running autopep8 with default settings). 

Comments accurately convey the purpose and / or meaning of the code block within the overall program.

Code is lightly commented without restating the code.

Complex logic, long code, or design-specific code is thoroughly explained. 

Comments are clear, full sentences beginning with a capital letter and ending in a full stop
3.2 pts
Credit
Formatted to the required PEP8 guidelines with two violations of any given rule. (including running autopep8 with default settings). 

Comments convey the purpose and / or meaning of the code block within the overall program.

Code is commented and may restate code.

Complex logic, long code, or design-specific code is thoroughly explained. 

Comments are clear, full sentences ideally beginning with a capital letter and ending in a full stop.
2.8 pts
Pass
Formatted to the required PEP8 guidelines with three violations of any given rule (including running autopep8 with default settings).

Writes sensible comments which describe the purpose and / or meaning of the code block within the overall program.

Complex logic, long code, or design-specific code is explained. 

Comments are clear, full sentences.
2 pts
Fail
Not yet able to format to the required PEP8 guidelines with three or less violations of any given rule (including running autopep8 with default settings).

Not yet able to write sensible comments which describe the purpose and / or meaning of the code block within the overall program.

Not yet able to explain complex logic, long code, or design-specific code. 

Not yet able to write comments which are clear, full sentences.
0 pts
	
/4 pts
Criterion 5: Testing
	
High Distinction
Write a test suite using the Pytest framework for testing each testable class for each project.

Unit tests written are used to prove the behaviour is robust and outputs/results are as expected.

Unit tests thoroughly test expected behaviour, relevant boundary conditions, and invalid cases where appropriate.

Test suite includes multiple fixtures per class type being tested.

Provide coverage report with 95% coverage.

Consistent testing approach throughout and developed synchronously with your program.
4 pts
Distinction
Write a test suite using the Pytest framework for testing each testable class  for each project.

Unit tests written are used to prove the behaviour is robust and outputs/results are as expected.

Unit tests test expected behaviour and relevant boundary or invalid cases where appropriate.

Test suite includes fixtures with all classes represented once.

Provide coverage report with 85% coverage.

Consistent testing approach throughout and developed synchronously with your program.
3.2 pts
Credit
Write a test suite using the Pytest framework for testing each testable class in Project 1 or 3.

Unit tests written are used to prove the behaviour is robust and outputs/results are as expected.

Unit tests test expected behaviour and some relevant alternative or boundary cases.

Test suite includes fixtures.

Provide coverage report with 70% coverage.
2.8 pts
Pass
Write a test suite using the Pytest framework for testing classes in the Project 1 or 3.

Unit tests written are used to prove the behaviour is robust and outputs/results are as expected.

Provide coverage report with 60% coverage.
2 pts
Fail
Not yet able to write a test suite using the Pytest framework for testing classes in the program for a project.

Not yet able to write unit tests to prove the behaviour is robust and outputs/results are as expected.
0 pts
	
/4 pts
Criterion 6: Feedback, Code Review, & Incremental Development
	
High Distinction
Incrementally develop all projects within the portfolio.

Perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Write and describe the link between the code adjusted and the learning experience from the discussion.

Provide multiple pieces of evidence of the code changed and concepts learned from that experience.

Demonstrates clearly reasoned justifications of meaningful decisions made.

Communicates justifications and links succinctly.
4 pts
Distinction
Incrementally develop all projects within the portfolio.

Perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Write and describe the link between the code adjusted and the learning experience from the discussion.

Provide some pieces of evidence of the code changed and concepts learned from that experience.

Demonstrates reasoned justifications of meaningful decisions made.

Communicates justifications and links succinctly.
3.2 pts
Credit
Incrementally develop all projects within the portfolio.

Perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Write and describe the link between the code adjusted from the discussion.

Provide evidence of the code changed and identify concepts learned from that experience.

Explains decisions made following the feedback.

Communicates justifications and links well.
2.8 pts
Pass
Incrementally develop all projects within the portfolio.

Perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Write and describe the link between the code adjusted from the discussion.

Provide some pieces of evidence of the code changed.

Demonstrates reasoned justifications of decisions made.

Communicates justifications and links well.
2 pts
Fail
Not yet able to incrementally develop all projects within the portfolio.

Not yet able to perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Not yet able to write and describe the link between the code adjusted from the discussion.

Not yet able to provide some pieces of evidence of the code changed.

Not yet able to demonstrate reasoned justifications of decisions made.

Not yet able to communicate justifications and links well.
0 pts
	
/4 pts

Choose a submission type