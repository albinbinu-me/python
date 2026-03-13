import time

# times = int(input("enter the time in seconds: "))
# for i in reversed(range(1,6)):
#     print(i)
#     time.sleep(times) # for delay
# print("happy new year")


my_time = int(input("enter the time: "))
#        range(start,stop,step)
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    time.sleep(1)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
print('time up')