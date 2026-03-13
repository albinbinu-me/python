"""
for loop - execute a block of code a fixed number of times
           can iterate over string,range,sequence

reversed - is a func for reverse.

loop control statement's - continue,break
"""

# for i in reversed(range(0,11)):
#     print(i)
# print("happy new year")


#        range(start,stop,step)
# for i in range(0,11,2):
#     print(i)

# credit_card = '1234-5678-0123'
# for i in credit_card:
#     print(i,end="")

# continue

for i in range(0,21):
    if i == 13:
        continue
    print(i,end=",")
