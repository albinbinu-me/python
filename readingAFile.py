try:
   with open('test.txt') as file:
       print(file.read())
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)