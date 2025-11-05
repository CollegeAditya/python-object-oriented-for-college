class Person:
    def get_roll(self):
        return "Generic Person Roll"

class Student(Person):
    def get_roll(self):
        return "Student Roll: 101"

class Staff(Person):
    def get_roll(self):
        return "Staff Roll: S001"

class Grade:
    def Calculate(self, m1, m2=None):
        if m2 is None:
            return m1
        else:
            return (m1 + m2) / 2

class Score:
    def __init__(self, Marks):
        self.Marks = Marks
    def __add__(self, other):
        return Score(self.Marks + other.Marks)
    def __str__(self):
        return str(self.Marks)

p = Person()
s = Student()
stf = Staff()
print(p.get_roll())
print(s.get_roll())
print(stf.get_roll())

g = Grade()
print(g.Calculate(80))
print(g.Calculate(80, 90))

s1 = Score(75)
s2 = Score(85)
s3 = s1 + s2
print(s3)
