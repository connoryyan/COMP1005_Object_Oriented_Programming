Programming Portfolio: Checkpoint
Criteria	Ratings	Points
Criterion 1: Object-Oriented Design & Modelling
view longer description
	
High Distinction
Demonstrate exceptional object-oriented design, including complete adherence to Object-Oriented principles of encapsulation, and the S and O of SOLID design principles. 

Composition, aggregation, and association are meaningfully and accurately applied within the diagrams and programs where appropriate. 

Relationships (Arrows, multiplicity, and labels) are correctly modelled. 

Chosen classes are appropriate for the problem being solved and model the real world.
  
Only uses Object-Oriented concepts taught within the course and are meaningful to the problem being solved. No external libraries are used which are not used in the course.
4 pts
Distinction
Demonstrates well-rounded object-oriented design, including complete adherence to Object-Oriented principles of encapsulation, and demonstrates application of S and O of SOLID design principles. 

Composition, aggregation, and association are meaningfully and accurately applied within the diagrams and programs where appropriate. 

Arrows, multiplicity, and labels are correctly written. 

Chosen classes are appropriate for the problem being solved and model the real world.
  
Only uses Object-Oriented concepts taught within the course and are meaningful to the problem being solved. No external libraries are used which are not used in the course.
3 pts
Credit
Demonstrates foundational object-oriented design, including complete adherence to Object-Oriented principles of encapsulation, and the S with consideration of O of SOLID design principles. 

Composition, aggregation, and association are mechanically applied within the diagrams and programs where appropriate. 

Arrows are correctly written and multiplicity and labels mostly align with the code. 

Chosen classes are appropriate for the problem being solved or to demonstrate a relationship and model the real world.
  
Only uses Object-Oriented concepts taught within the course and are meaningful to the problem being solved. No external libraries are used which are not used in the course.
2 pts
Pass
Demonstrates foundational object-oriented design, including adherence to Object-Oriented principles of encapsulation and consideration of S and O of SOLID design principles.  

Composition, aggregation, and association are mechanically applied within the diagrams and programs where appropriate. 

Arrows are correctly written. 
Multiplicity and labels align with the code for at least one relationship. 

Chosen classes are appropriate for the problem being solved or to demonstrate a relationship and model the real world.
  
Only uses Object-Oriented concepts taught within the course and are meaningful to the problem being solved. No external libraries are used which are not used in the course.
1 pts
Fail
Not yet able to demonstrate basic object-oriented design, including some adherence to Object-Oriented principles of encapsulation, and the S and O of SOLID design principles. 

Not yet able to implement composition, aggregation, and / or association within the diagrams and programs. 

Not yet able to show arrows, multiplicity, and / or labels correctly. 

Not yet able to choose classes which are appropriate for the problem being solved and model the real world.
  
Not yet able to use Object-Oriented concepts taught within the course and are meaningful to the problem being solved. No external libraries are used which are not used in the course.
0 pts
	
4/4 pts
CommentGood UML.

We'd usually make id private and provide a getter to make it read-only so other developers can't accidentally alter it.

To note, because the Client/Branch relationship says a Client may have 0 or 1 preferred Branch, the preferred_branch would technically be `Branch | None`, instead of just `Branch`.

You can exclude the str()/repr() methods from the UML, as they don't change how the system works.
Criterion 2: Object-Oriented Implementation
view longer description
	
High Distinction
Functionality implementation is logical and correct for what operation is being achieved. 

Specifications surrounding required functionality are completely adhered to. 

Code matches class diagram and chosen classes, data types, and attributes are appropriate and meaningful to the problem being solved.
4 pts
Distinction
Functionality implementation is logical and correct for what operation is being achieved. 

Specifications surrounding required functionality are completely adhered to. 

Code closely resembles class diagram and chosen classes, data types, and attributes are appropriate and meaningful to the problem being solved.
3 pts
Credit
Functionality implementation is logical and correct for what operation is being achieved. 

Specifications surrounding required functionality are mostly adhered to. 

Code matches the UML entities (classes, data types, and attributes) are appropriate and meaningful to the problem being solved.
2 pts
Pass
Functionality implementation is logical and mostly correct for what operation is being achieved. 

Specifications surrounding required functionality are somewhat adhered to. 

Code closely resembles class diagram and chosen classes, data types, and attributes are appropriate and meaningful to the problem being solved.
1 pts
Fail
Not yet able to implement functionality which is logical and correct for what operation is being achieved.

Not yet able to adhere to core required functionality. 

Not yet able to implement code which represents the class diagram and chosen classes, data types, and attributes are appropriate and meaningful to the problem being solved.
0 pts
	
3/4 pts
CommentExcellent implementation.

The relationship between Client and Account states that all Accounts will be owned by at most 1 Client. However, this is never enforced in the code.
Criterion 3: Code Quality and Structure
view longer description
	
High Distinction
Formatted to the required PEP8 guidelines (including running autopep8 with default settings). 

File structure demonstrates one class per module and imported as necessary. 

Code contains no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Completely consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed and all parameters are purposeful to the method.
4 pts
Distinction
Formatted to the required PEP8 guidelines (including running autopep8 with default settings). 

File structure demonstrates one class per module and imported as necessary. 

Code minimal to no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Mostly consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed and all parameters are purposeful to the method.
3 pts
Credit
Formatted to the required PEP8 guidelines (including running autopep8 with default settings). 

File structure demonstrates one class per module and imported as necessary. 

Code minimal to no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Mostly consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed and all parameters have a use.
2 pts
Pass
Formatted to the required PEP8 guidelines (including running autopep8 with default settings). 

File structure demonstrates one class per module and imported as necessary. 

Code minimal to no extraneous elements, including dead code, redundant code, or hard-coded elements. 

Somewhat consistent code and problem-solving approach throughout. 

Method definitions describe the operation being performed.
1 pts
Fail
Not yet able to format to the required PEP8 guidelines (including running autopep8 with default settings). 

Not yet able to structure files indicating one class per module and imported as necessary. 

Not yet able to write exclude extraneous elements, including dead code, redundant code, or hard-coded elements. 

Not yet able to write consistent code and problem-solving approach throughout. 

Not yet able to define methods which describe the operation being performed.
0 pts
	
4/4 pts
CommentExcellent code structure.
Criterion 4: Documentation & Professional Practice
view longer description
	
High Distinction
Comments accurately convey the purpose and / or meaning of the code block within the overall program.

Code is lightly commented without exactly restating the code.

Complex logic, long code, or design-specific code is clearly and thoroughly explained. 

Comments are clear, full sentences beginning with a capital letter and ending in a full stop.

A class docstring is written for each class.
4 pts
Distinction
Comments accurately convey the purpose and / or meaning of the code block within the overall program.

Code is lightly commented without exactly restating the code.

Complex logic, long code, or design-specific code is thoroughly explained. 

Comments are clear, full sentences beginning with a capital letter and ending in a full stop.
3 pts
Credit
Comments convey the purpose and / or meaning of the code block within the overall program.

Code is commented without exactly restating the code.

Complex logic, long code, or design-specific code is thoroughly explained. 

Comments are clear, full sentences beginning with a capital letter and ending in a full stop.
2 pts
Pass
Writes sensible comments which describe the purpose and / or meaning of the code block within the overall program.

Complex logic, long code, or design-specific code is explained. 

Comments are clear, full sentences ideally beginning with a capital letter and ending in a full stop.
1 pts
Fail
Not yet able to write sensible comments which describe the purpose and / or meaning of the code block within the overall program.

Not yet able to explain complex logic, long code, or design-specific code. 

Not yet able to write comments which are clear, full sentences ideally beginning with a capital letter and ending in a full stop.
0 pts
	
4/4 pts
CommentExcellent comments.
Criterion 5: Integration Testing & Main
view longer description
	
High Distinction
Integration test written in the main module prove the objects interact as expected.

All objects are thoroughly tested and demonstrate all capable methods. 

Multiple objects of the same type are instantiated with different attribute values and tested.

Clear comments are provided to describe the methods being ran.
4 pts
Distinction
Integration test written in the main module prove the objects interact as expected.

All objects are thoroughly tested and demonstrate all capable methods. 

Multiple objects of the same type are instantiated with different attribute values and tested.
3 pts
Credit
Integration test written in the main module prove the objects interact as expected.

Most objects are thoroughly tested and demonstrate all capable methods. 

Multiple objects of the same type are instantiated with different attribute values and tested.
2 pts
Pass
Integration test written in the main module prove the objects interact as expected.

Most objects are tested and demonstrate most capable methods. 

Many objects of the same type are instantiated with different attribute values and tested.
1 pts
Fail
Not yet able to write integration tests written in the main module prove the objects interact as expected.

Not yet able to test and demonstrate capable methods of objects. 

Not yet able to instantiate objects of the same type are instantiated with different attribute values and tested.
0 pts
	
4/4 pts
CommentAll meaningful methods are tested. Good comments.
Criterion 6: Feedback, Code Review, & Incremental Development
view longer description
	
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
3 pts
Credit
Incrementally develop all projects within the portfolio.

Perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Write and describe the link between the code adjusted from the discussion.

Provide some pieces of evidence of the code changed and concepts learned from that experience.

Demonstrates reasoned justifications of decisions made.

Communicates justifications and links well.
2 pts
Pass
Incrementally develop all projects within the portfolio.

Perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Write and describe the link between the code adjusted from the discussion.

Provide some pieces of evidence of the code changed.

Demonstrates reasoned justifications of decisions made.

Communicates justifications and links well.
1 pts
Fail
Not yet able to incrementally develop all projects within the portfolio.

Not yet able to perform a code review with your workshop supervisor, once per week. Describe at least one change, tip, or feedback you received and implemented.

Not yet able to write and describe the link between the code adjusted from the discussion.

Not yet able to provide some pieces of evidence of the code changed.

Not yet able to demonstrate reasoned justifications of decisions made.

Not yet able to communicate justifications and links well.
0 pts
	
4/4 pts
