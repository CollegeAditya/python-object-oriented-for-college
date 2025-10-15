class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, employee_id):
        super().__init__(name, age)
        self.subject = subject
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class ClassTeacher(Teacher):
    def __init__(self, name, age, subject, employee_id, class_name, num_students):
        super().__init__(name, age, subject, employee_id)
        self.class_name = class_name
        self.num_students = num_students

    def display(self):
        super().display()
        print(f"Class in charge: {self.class_name}")
        print(f"Number of students: {self.num_students}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting for class {self.class_name}.")
