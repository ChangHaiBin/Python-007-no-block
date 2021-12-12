# Feel free to play with this simple example.
# The actual question is in the next file.
#
# We assume that the bank will close the account if the remaining balance is less than $1.

amount = 10000
while amount >= 1:
    print("=====")
    print(f"You have ${amount} remaining. ")
    print("How much do you want to withdraw?")
    withdrawal = float(input())
    if withdrawal > amount:
        print(f"Your withdrawal amount of ${withdrawal} is more than your account balance of ${amount}. Your transaction has been denied.")
    else:
        amount = amount - withdrawal
        print(f"After withdrawing ${withdrawal}, you have ${amount} remaining")


print("Your account has less than $1. We will close your account.")
