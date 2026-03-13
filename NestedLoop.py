"""
a loop inside another loop
"""


# for x in range(3):
#     for y in range(0,10):
#         print(y,end=",")
#     print('')


rows = int(input("enter number of rows: "))
column = int(input("enter no.of column: "))
symbol = input("enter the symbol: ")

for i in range(rows):
    for j in range(column):
        print(symbol,end='')
    print()