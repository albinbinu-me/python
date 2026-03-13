# while loop execute the code WHILE some condition remain true

# eg - 1

# name = input("enter your name: ")
# while name == "":
#     print("you didn't your name")
#     name = input("enter your name: ")
# print(f'hello {name}')

# eg - 2

# age = int(input("enter your age: "))
# while age < 0:
#     print("Age can't be negative number")
#     age = int(input("enter your age: "))
# print(f"you're {age} years old")

# eg - 3

# food = input("enter the food you like (q - quit): ")
# while not food == 'q':
#     print(f"you like {food}")
#     food = input("enter another food you like (q - quit):")
# print("bye")

# eg - 4

number = int(input("enter a number between 1 - 10: "))

while number < 1 or number > 10:
    print("invalid number")
    number = int(input("enter a number between 1 - 10: "))
print(f"your number is {number}")
