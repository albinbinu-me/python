import random

x = random.randint(1,6) # random number btw 1 ~ 6
y = random.random() # random number btw 0 ~ 1

fruits = [
    "Apple","orange","grapes","melon","tomato"
]

z = random.choice(fruits) # it give random choices

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards) # shuffle the list!
print(cards)