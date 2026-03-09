"""
copyfile() = copies contents of a file
copy() = copyfile() + permission mode + destination can be a dir
copy2() = copy() + copies metadata

"""

import shutil


src = "test.txt"
destination = "C:\\Users\\albin\\OneDrive\\Documents\\copy.txt"

# src, desti
try:
    action = shutil.copyfile(src,destination)
    if action:
        print("copied")
    else:
        print("something")
except Exception as e:
    print(e)