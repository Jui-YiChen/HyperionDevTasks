age = int(input("What is your age?")) #request for input of age

'''I found originally when I put age between 40 and 65, it will only show "You're over the hill, so I probably should
rearrange from age > 100 to >65 >40... but I chose to limit 40-64 just for the simplisity of this task'''


if 40<= age < 65:
    print("You're over the hill.")
elif age >= 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age <= 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")