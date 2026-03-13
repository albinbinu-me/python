"""

A = p(1 + r/n) ^t
A = final amount
p = principal balance
r = interest rate
t = time
"""


principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("enter principle amount: "))
    if principle <= 0:
        print("principle cant be ZERO")

while rate <= 0:
    rate = float(input("enter the rate: "))
    if rate <= 0:
        print("rate cant be ZERO")

while time <= 0:
    time = int(input("enter the time: "))
    if time <= 0:
        print("time cant be zero")

final_amount = principle * pow((1 + rate / 100),time)

print(f'total amount is {final_amount}')