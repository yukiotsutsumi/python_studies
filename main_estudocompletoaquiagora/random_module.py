import random  # pseudo-random

x = random.randint(1, 6)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
cards = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)