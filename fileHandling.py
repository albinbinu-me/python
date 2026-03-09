import os

path = 'C:\\Users\\albin\\OneDrive\\Desktop\\test'

if os.path.exists(path):
    print("it's a valid path")
    if os.path.isfile(path):
        print("its a file")
    elif os.path.isdir(path):
        print("it's a dir")

else:
    print("not exist")