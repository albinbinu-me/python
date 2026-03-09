animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the "+ item)

# print("The {} jumped over the {}".format(animal,item))

# positional argument's

# print("The {0} jumped over the {1}".format(animal,item))

# print("The {1} jumped over the {0}".format(animal,item))

# keyword args
# dont need varibles
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))
# print("The {item} jumped over the {animal}".format(animal="cow",item="moon"))

# another method
# text = "The {} jumped over the {}"
# print(text.format(animal,item))


# add padding

# name = "bro"
# print("hello, my name is {}".format(name)) # without padding
# # print("hello, my name is {:10} i'm fine".format(name)) # with padding ->
# print("hello, my name is {:>10} i'm fine".format(name))
# print("hello, my name is {:<10} i'm fine".format(name))
# print("hello, my name is {:^10} i'm fine".format(name))

# position number's

number = 3.14159

print("The number is {:.2f}".format(number))