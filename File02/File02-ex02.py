import random

# You want to create a snakes-and-ladder game.
# In particular, create a function that does the following:
#     If you land on position 2, move forward to position 8
#     If you land on position 5, move forward to position 9
#     Else, you stay at that location
def move_forward_if_possible(original_position):
    ..........................




position = 0
print(f"You are currently in position {position}. Press ENTER to roll a dice.")
input()

dice = random.randint(1,6)
position = position + dice
print(f"You are now at {position}. Checking if any ladders to climb:")

position = move_forward_if_possible(position)
print(f"Your final position is {position}.")
