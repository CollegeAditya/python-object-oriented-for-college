class student:
     def __init__(self, name, roll, marks):
         self.name = name
         self.roll = roll
         self.marks = marks
     def details(self):
         print(f"name: {name}, roll: {roll}, marks: {marks}")
     def grade(self):
         if (self.marks >= 40): print("pass")
         else: print("fail")

one = student("zoro", 1, 92)
two = student("goku", 2, 98)
