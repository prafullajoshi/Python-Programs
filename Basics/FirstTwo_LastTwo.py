#Write a program to accept a string from user and display a string made of 1st two & last two character. Alternate characters.
#Hint: display alternate character starting with 1.

#!/usr/bin/python
def printString(string):
	print(string[:2]+""+string[-2:])
	print(string[::-1])
def main():
	string = input("Enter the string :")
	printString(string)
if __name__=="__main__":
	main()	
