import random

again = True

while again:
    print(random.randint(1,6))
    onemore_roll = input("Want to do one more dice roll? (y/n): ")
    if onemore_roll.lower() == "y":
        continue
    else:
        breaky