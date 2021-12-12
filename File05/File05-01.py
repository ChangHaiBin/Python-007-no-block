import random
location = 1
while location < 30:
    print("=====")
    print(f"You are currently at {location}")
    input("Press ENTER to roll a dice")
    dice = random.randint(1, 6)
    location = location + dice
    print(f"You are now at {location}")
    if location == 3:
        print("You found a stairs! Climbing stairs to 22")
        location = 22
    elif location == 5:
        print("You found a stairs! Climbing stairs to 8")
        location = 8
    elif location == 11:
        print("You found a stairs! Climbing stairs to 26")
        location = 26
    elif location == 20:
        print("You found a stairs! Climbing stairs to 29")
        location = 29
    elif location == 17:
        print("You encounter a snake! Slide back down to 4")
        location = 4
    elif location == 19:
        print("You encounter a snake! Slide back down to 7")
        location = 7
    elif location == 21:
        print("You encounter a snake! Slide back down to 9")
        location = 9
    elif location == 27:
        print("You encounter a snake! Slide back down to 1")
        location = 1


print("You have reached position 30. You win!")
