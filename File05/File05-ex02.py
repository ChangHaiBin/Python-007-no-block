import random

# Complete the following "give_hint" function,
# So that we can let the user know whether
# their guess is larger or smaller than the actual answer.
#
# This "give_hint" function will only print out messages, but returns nothing.
def give_hint(guess, answer):
    # ...............
    print("Hello")




##########################################################

answer = random.randint(1, 100)
print("A random number from 1 to 100 has been generated")
guess = -1

while guess != answer:
    print("Please guess the number:")
    guess = int(input())
    give_hint(guess=guess, answer=answer)

print("You win!")
