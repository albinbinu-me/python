"""
#      os.remove - for delete file
       os.rmdir for remove empty dir
       shutil.rmtree - remove dir contain files
"""
import os

# remove file

# import os
#
# src = 'test'
#
# try:
#     os.remove(src)
#     print("file is removed")
# except FileNotFoundError as e:
#     print("file not found")


# # remove dir
# import os
# path = 'test'
#
# try:
#     os.remove(path)
#     print(path,"removed")
# except FileNotFoundError:
#     print("dir not found")
# except PermissionError:
#     print("access denied")


# remove dir contain files

import shutil
path = 'test'
try:
    shutil.rmtree('test')
    print(path,"removed")
except FileNotFoundError:
    print("dir not found")
except PermissionError:
    print("access denied")
