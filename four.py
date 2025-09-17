string = input("enter the string: ")
count = 0
vowels = ["a", "e", "i", "o", "u"]

for i in string:
    if i in vowels:
        count += 1

print(count)