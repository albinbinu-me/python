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

# name = "hp" # -> global scope
#
# def display_name():
#     name = "lenovo" # local scope
#     print(name)
#
# print(name)

"""
args parameter
it will pack all args to a tuple
"""

# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(sum(1,2,3,4,5))

# def sum(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 22
#     for i in args:
#         sum += i
#     return sum
#
# print(sum(1,2,3))

"""
**kwargs -> pack them into dict, 
"""
def display_name(**kwargs):
    # print("hello",kwargs['firstName'],kwargs['lastName']) method 1
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


display_name(title="mrs",firstName="rohini",lastName="pk")