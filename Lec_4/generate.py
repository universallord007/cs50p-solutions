import random

# coin = random.choice(["Heads","Tails"])
# print(coin)


# This takes a random number between the two numbers that the user inputs and prints it out.
# x = int(input("Enter the first number that you want the random choice within : "))
# y = int(input("Enter the second number that you want the random choice within : "))

# number = random.randint(x,y)
# print(number)

cards = ["jacks","queens","kings","aces"]
random.shuffle(cards)
# This shuffles the order of the cards in the list and then prints them out one by one.
for card in cards :
    print(card)