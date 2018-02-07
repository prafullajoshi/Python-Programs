#Write a program to accept 2 strings from user and swap 1st 2 characters of each of them.

#!/usr/bin/python
def printString(string1,string2):
	print(string2[:2]+""+string1[2:])
	print(string1[:2]+""+string2[2:])
def main():
	string1 = input("Enter 1st string :")
	string2 = input("Enter 2nd string :")
	printString(string1,string2)
if __name__=="__main__":
	main()	
