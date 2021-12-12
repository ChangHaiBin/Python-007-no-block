import random
# Take a look at the following code, feel free to play with the game.
# The actual question will be in the next file

answer = random.randint(1, 100)
print("A random number from 1 to 100 has been generated")
guess = -1

while guess != answer:
    print("Please guess the number:")
    guess = int(input())
    if guess < answer:
        print(f"Your guess of {guess} is less than the actual answer.")
    elif guess > answer:
        print(f"Your guess of {guess} is more than the actual answer.")
    else:
        print("You have gotten the right answer.")

print("You win!")
