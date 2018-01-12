# Exercise 2, Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

n = int(input("Give us a random number you like: "))
if n%2 == 0:
	print("Your favorite number is even!")
	if n%4 == 0:
		print("It is also divisible by 4 to give "+str(n/4))
else:
	print("Your favorite number is odd!")

m = int(input("Now give us another number: "))
if n%m == 0:
	print("It is divisible by your favorite number to give "+str(n/m))
else:
	print("It is not divisible by your favorite number :(")
