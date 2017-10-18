"""
Exercise 2: Odd or Even

Ask the user for a number. Depending on whether the number is even or odd, 
	print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
number = int(input("Please input an integer: "))
check = int(input("Please input a number to check: "))

if number % 2 == 0:
	print("Number is even")
else:
	print("Number is odd")

if number % 4 == 0:
	print ("Number is also a multiple of 4")

if number % check == 0:
	print (number, " can be evenly divided with ", check)

input()