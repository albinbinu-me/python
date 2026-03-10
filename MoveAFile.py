import os

src = 'test.txt'
destination = 'C:\\Users\\albin\\OneDrive\\Desktop\\test.txt'

try:
    if not os.path.exists(src):
        print("src doesn't exist")
    elif os.path.exists(destination):
        print("file already exist the destination")
    else:
        os.replace(src,destination)
        print("file has been moved")
except Exception as e:
    print(e)