foods  = []
prices = []
total = 0


while True:
    food = input("enter a food to buy: (q - quit): ").lower()
    if food == 'q':
        break
    else:
        price = float(input(f"enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print('----- YOUR CART -----')
for f in foods:
    print(f)
print('\n----- TOTAL PRICE -----')
for p in prices:
    total = total + p
print()
print(f'total is {total}')