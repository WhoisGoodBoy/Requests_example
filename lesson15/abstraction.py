from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    @abstractmethod
    def do_work(self):
        pass

    def some_logic(self):
        print('some logic')

class ToyotaEmployee(Employee):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)

    def do_work(self):
        print('I`m doing work of Toyota Employee')

class ATBEmployee(Employee):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)

john = ToyotaEmployee('John', 18, 'assembler', 3000)
john.do_work()
#marcus = ATBEmployee('Marcus', 1, 'child', 'love')
#marcus.do_work()
nataniel = Employee('Nataniel', 2, 'child', 'love')


