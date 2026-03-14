fruits = ['Apple','Orange','banana','coconut']
vegtables = ['carrot','tomato','potato']
meats = ['chicken','fish','mutton']

groceries = [fruits,vegtables,meats]

# print(groceries[1][1])

# iteration through 2d list
# for i in groceries:
#     print(i)


# for loop for iterating each values
for items in groceries:
    for foods in items:
        print(foods,end=' ')
    print()

# while loop for iterating each values
# i = 0
# while i < len(groceries):
#     j = 0
#     while j < len(groceries[i]):
#         print(groceries[i][j])
#         j += 1
#     i += 1
