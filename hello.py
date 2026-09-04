def calculate_square(number:int):
    return number * number

print(calculate_square(9))

def calculate_add(number:int):
    return number + number

print(calculate_add(4444))

def calculate_subtract(number:int):
    return number - number

print(calculate_subtract(6764))

def calculate_subtract(number:int):
    return number - number

print(calculate_subtract(6764))

print("frtctfv")

print("Siblings are annoying: true or false?") 
siblings = input()

if siblings == "true":
    print("Sibling are annoying!!!")
else:
    print("No they are not!!")


print("What is your first number?")
number = int(input())
print("What is your operation?")
operation = input()
print("What is your second number?")
n = int(input())
if operation == "+":
    answer = number + n
elif operation == "-":
    answer = number - n
elif operation == "*":
    answer = number * n
elif operation == "/":
    answer = number / n
else:
    print(f"{operation} not vaild")

print(answer)