string = input("enter the string: ")
i = 0

while i < len(string):
    string.replace("-", ",")
    i+=1

print(string)