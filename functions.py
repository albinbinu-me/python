"""
function is A BLOCK OF CODE only executed when we called
"""

# def hello(fname,lname,age):
#     print("hello " + fname +" "+ lname)
#     print("you're "+ str(age))
#
#
# hello("Albin","b",21)

"""

return - send a py value back to the caller. 

"""


# def mult(x,y):
#     return x * y
#
# sum = mult(2,3)
# print(sum)

"""
:keyword args
"""
# def wish(firstName,lastName):
#     print("hello " + firstName + " " + lastName)
#
# wish(lastName="binu",firstName="Albin")

"""
nested function calls
"""

"""
print
round
abs
float
input
"""
# print(abs(round(float(input("enter the number: ")))))

"""
scope -> a regional that a variable is aceesed
"""

name = "hp" # -> global scope

def display_name():
    name = "lenovo" # local scope
    print(name)

print(name)