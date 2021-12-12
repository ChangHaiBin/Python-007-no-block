import random


def add_dice_roll(original_location):
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}")
    new_location = original_location + dice
    print(f"You are now at {new_location}")
    return new_location


def climb_stairs_if_possible(original_location):
    if original_location == 3:
        print("You found a stairs! Climbing stairs to 22")
        new_location = 22
    elif original_location == 5:
        print("You found a stairs! Climbing stairs to 8")
        new_location = 8
    elif original_location == 11:
        print("You found a stairs! Climbing stairs to 26")
        new_location = 26
    elif original_location == 20:
        print("You found a stairs! Climbing stairs to 29")
        new_location = 29
    else:
        new_location = original_location
    return new_location


def slide_down_snake_if_necessary(original_location):
    if original_location == 17:
        print("You encounter a snake! Slide back down to 4")
        new_location = 4
    elif original_location == 19:
        print("You encounter a snake! Slide back down to 7")
        new_location = 7
    elif original_location == 21:
        print("You encounter a snake! Slide back down to 9")
        new_location = 9
    elif original_location == 27:
        print("You encounter a snake! Slide back down to 1")
        new_location = 1
    else:
        new_location = original_location
    return new_location


location = 1
while location < 30:
    print("=====")
    print(f"You are currently at {location}")
    input("Press ENTER to roll a dice")
    location = add_dice_roll(location)
    location = climb_stairs_if_possible(location)
    location = slide_down_snake_if_necessary(location)

print("You have reached position 30. You win!")
