# Complete the following function, so that:
#
# If withdrawal is less than or equal to the balance,
#    then deduct the withdrawal, print out messages, and
#        RETURNS the remaining balance.
#
# Else, if withdrawal exceeds the balance
#    prints out an error message, and
#        RETURNS the original balance, unchanged.
def withdraw_money_if_possible(amount, withdrawal):
    return amount


amount = 10000
while amount >= 1:
    print("=====")
    print(f"You have ${amount} remaining. ")
    print("How much do you want to withdraw?")
    withdrawal = float(input())
    amount = withdraw_money_if_possible(amount=amount, withdrawal=withdrawal)


print("Your account has less than $1. We will close your account.")
