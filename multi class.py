class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
      
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Certification:
    def __init__(self, certification_name):
        self.certification_name = certification_name

    def display_certification(self):
        print(f"Certification: {self.certification_name}")

class Trainer(Employee, Certification):
    def __init__(self, name, age, employee_id, salary, certification_name):
        Employee.__init__(self, name, age, employee_id, salary)
        Certification.__init__(self, certification_name)

    def display(self):
        Employee.display(self)
        Certification.display_certification(self)
