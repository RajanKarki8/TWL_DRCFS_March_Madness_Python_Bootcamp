class Person:
    def __init__(self, name, age , address):
        self.name = name
        self.age = age
        self.address = address
        
    def greet(self):
        return f'good morning {self.name}'
    
p1 = Person('Kushal', '17', 'Jhapa')

#print(p1.greet())

class Employee(Person):
    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary
        
    def greet(self):
        return f'Good morning {p1.name}'
    
e1 = Employee('Manoj', '100', 'Jhapa', '70000')

print(e1.greet())