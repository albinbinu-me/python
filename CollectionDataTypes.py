"""
list = [] ordered and changeable, Duplicate Ok
set = {} unordered and immutable, but Add/remove. No duplicates
Tuple = () ordered and unchangeable. duplicates, faster
"""
# list
# fruits = ['apple','orange','banana','coconut']


# start:end(exclude)
# print(fruits[0:3])
# loop
# for i in fruits:
#     print(i)

# for get all list methods.
# print(dir(fruits))

#length func
# print(len(fruits))

# in function
# print('pineapple' in fruits)

# change value
# fruits[0] = "pineapple"

# append will insert element to the last of the list
# fruits.append('grapes')

# remove method removes the item
# fruits.remove('apple')

# insert will value to the list
# fruits.insert(0,"banana")

# it will sort the list
# fruits.sort()

# reverse the list
# fruits.reverse()

# proper reverse
# fruits.sort()
# fruits.reverse()

# clear the list
# fruits.clear()

# find index

# print(fruits.index('apple'))
# print(fruits.index('grapes'))

# count - is used to check any duplicate present

# print(fruits.count('apple'))
# print(fruits.count('melons'))

# set

# fruits = {"apple","orange","banana","grapes","apple"}
# duplicate values wont worked

# fruits = {"apple","orange","banana","grapes"}
# length of fruits
# print(len(fruits))
# fruits.clear()

# we can add elements, but cant do insert, because it is unordered
# fruits.add('kiwi')

# fruits.remove('apple')

# print("pine apple" in fruits)

# removes the last element of the list
# fruits.pop()

# print(fruits)

# fruits = ("apple","orange","banana","grapes")

# add duplicate values.
fruits = ("apple","orange","banana","grapes",)

# print(len(fruits))

# print("pineapple" in fruits)

# count is used to count the no. elements
# print(fruits.count('apple'))

for fruit in fruits:
    print(fruit)
