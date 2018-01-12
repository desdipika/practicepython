# Exercise 1, Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("What is your name?\n")
print("Hello there, "+name+"!")
age = input("How old are you?\n")
x = 100-int(age)
print("You will be a 100 years old in "+str(x)+" years!\n")
print("Thanks!")
