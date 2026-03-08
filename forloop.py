# for i in range(10):
#     print(i)


# for i in range(50,100):
#     print(i)

# for i in range(50,100,2):
#     print(i)

# for i in "lenovo":
#     print(i)

# import time
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)
# print("Good bye")


""" nested loop """
"""
the inner loop finish it's iterations before finishing outer loop
"""

# rows = int(input("enter the number of rows: "))
# colums = int(input("enter the number of colums: "))
# symbols = input("enter the symbols: ")
# for i in range(rows):
#     for j in range(colums):
#         print(symbols,end="")
#     print()


"""
break - terminated
continue - skip to the next iteration
pass - do nothing
"""

# break
# while True:
#     name = input("enter your name: ")
#     if name != "":
#         break

# continue
# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# pass

for i in range(1,20):
    if i == 13:
        pass
    else:
        print(i)