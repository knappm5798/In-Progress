# CTI-110
# P4HW1 - Expenses
# Michael Knapp
# 20200704
#

try:
    total=float(input('What is the starting amount in the account?' + ' Please enter postive number: '))

except ValueError:
    print("That wasn't a valid number, Try again")

print("You chose",total,"$")

expense=float(input("Please enter your first expense: "))

account = total
y = expense
total -= y

print("Your Net income is ",total,"$")

expense = print(input("Would you like to add an additional expense?: "))   
if expense (y or yes or Yes or YES or Y):
    y = float(input("What is your next expense?: "))
    total -= y
    print("Your Net income is:",total,"$")
else:
    print("Thank you for using my program! Your total is:",total,"$")




        