"""
collection which is ordered and unchangeable
used to group together interrelated data
"""

student = ("Bro",21,"male")

# print(student.count("Bro"))
# print(student.index("Bro"))

# for loop
# for i in student:
#     print(i)

# while loop

# i = 0
# while i < len(student):
#     print(student[i])
#     i += 1

# value exist

value = "Bro"

if value in student:
    print(value,"exist")
else:
    print(value,"not exist")