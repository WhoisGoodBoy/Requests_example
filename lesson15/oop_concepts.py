class Human:
    human_counter = []
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
class Employee(Human):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

john = Human('John', 2000, 'big boy')
entony = Employee('Entony', 1200, 'very big boy', '30000 souls', 'archangel')
entony.human_counter += 'entony'
john.human_counter += 'john'
print(john.age)
print(entony.position)
print(john.human_counter)
