"""

prevent the code from crashing

"""

try:
    firstNumber = int(input("enter first number: "))
    secondNumber = int(input("enter second number: "))
    answer = firstNumber / secondNumber
    print(answer)
except ZeroDivisionError as e:
    print(e)
    print("dividing by ZERO isn't allowed")
except ValueError as e:
    print(e)
    print("diving by value isn't possible")
except KeyboardInterrupt as e:
    print(e)
    print("keyboard is interrupted")
except Exception as e:
    print(e,"occurred")



