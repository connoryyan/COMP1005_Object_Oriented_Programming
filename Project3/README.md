# simbricks

## Workshop 7-2 24/9/2026

- Q: Not sure how to structure my project. Now there are 3 folders
  A: Do not yet try to implement all the thing. Make the project runnable first, and then draw a UML. If everything is ok, and all concept required by the rubric is met, then proceed with all your ideas.
- Q: What else do I need to do
  A: You need to make sure your code has all the concepts including inheritance, abstraction, capsulation, etc.
  - Before:
    ```py
    class Device():
    '''
    Simulate an electronic component of the robot. 
    '''
    def __init__(self, port: Port):
        self.port = port
    ```
  - After:
    ```py
    class Device(ABC):
    '''
    Simulate an electronic component of the robot. 
    '''
    def __init__(self, port: Port):
        self.port = port
    ```

## Workshop 8-1 19/10/2026

- Q: A `steppables` List is used for storing devices and objects that needs to be updated in `SimClock`. For adding a device, it will be $O(1)$, which is nice. But when doing romoval, it will be $O(n)$. I'm thinking will it be slow and should I use dictionary instead?
  A: $O(n)$ is actually an acceptable speed so you don't have to move to a dictionary. But I noticed that you are using
  ```py
  if steppable not in self._steppables:
      self._steppables.append(steppable)
  ```
  to avoid duplicates in your list, which is exacly what a set is doing. so I will recommend you to use a set instead of a list if the order of the devices is not important here.
    - Before: 
      ```py
      def __init__(self, step_ms: int = STEP_MS):
          self.step_ms = step_ms
          self.step_s = step_ms / 1000.0
          self.time_ms = 0
          self._steppables = [] # aggregation

      def add_device(self, steppable) -> None:
          '''
          Add a device which needs to be updated every frame
          '''
          if steppable not in self._steppables:
              self._steppables.append(steppable)

      def remove_device(self, steppable) -> None:
          if steppable in self._steppables:
              self._steppables.remove(steppable)
      ```
    - After: 
      ```py
      def __init__(self, step_ms: int = STEP_MS):
          self.step_ms = step_ms
          self.step_s = step_ms / 1000.0
          self.time_ms = 0
          self._steppables = set() # aggregation

      def add_device(self, steppable) -> None:
          '''
          Add a device which needs to be updated every frame
          '''
          self._steppables.add(steppable)

      def remove_device(self, steppable) -> None:
          self._steppables.discard(steppable)
      ```
- Q: I used list to store a gear train in a function to calculate gear ratio but not in a class. Is it OK?
  A: Idealy we want to see data structure being used in classes. But I think you can definitely also use lists to store gears in your class as well or you can make a new class for handling gears. And also the order of gears does really matter so list will be the best choice.
- Q: Since this is a simulation, there might be some concurrent events. Do you think I should implement some degree of concurrency in my project, or would it be better to avoid it?
  A: I would say no. Avoiding concurrency will prevent many unexpected errors. In fact, many simulations are single-threaded, so it would be better to keep it that way.
- A: You have many classes in one file (`pupdevices.py`). It's better to put classes in seperated files.
  Q: OK. So one file for one class right? But I think some devices have some relationship, like actuator classes `Actuator`, `DCMotor`, and `Motor`. Can I put these classes in one file.
  A: Yes.

## Workshop 9-2 29/10/2026

- Q: I'm trying to seperate classes in `pupdevices.py` into different files. But that means when I want to import them, it will be extreme messy. So can I make another file, and import all those files, and when I want to use a device, I just need to import this new file.
  A: Yes. It is not covered in this course, but, since you mentioned, what you talked about is called modules in python. And this is how we usually manage files in real development.
  - Before:
    ```
    |- pupdevices.py
    ```
  - After:
    ```
    |-- pupdevices
    |  |-- __init__.py
    |  |-- actuator.py
    |  |-- device.py
    ```
- Q: I have fixtures stores accounts:
  ```py
  @pytest.fixture
  def savings_account(self):
      account = SavingsAccount(1, 0.05)
      account.deposit(500.0)
      return account
  ```
  I know how fixture works. But actually I can do the same job with a regular function that return me a well-initialised `Account` object. So what is the different.
  A: Fixture can enable you to have a same object for different tests. So if you have a function and want to achieve this, you will need to first define this function
  ```py
  def savings_account(self):
      account = SavingsAccount(1, 0.05)
      account.deposit(500.0)
      return account
  ```
  Then in the test you will need to store the return value of it in a variable first. So fixture can save you this line of code.
- Q: I have this fixture which return me a list of two fixtures. Shall I keep this as a fixture or I can actually have this as a regular function?
  ```
  @pytest.fixture
  def accounts(self, savings_account, everyday_account):
      return [
          savings_account,
          everyday_account
      ]
  ```
  A: Keep it as a fixture, so that you can use it freely without calling it and then store return value in a variable.
  Q: So can I say fixture is like a constant in an regular class?
  A: Yes.

## Workshop 10-1 2/11/2026
