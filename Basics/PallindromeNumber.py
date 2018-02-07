#Write a program to take number from user & check if its palindrome or not

#!/usr/bin/python
def isPallindrome(number):
	originalNumber=number
	reverse=0
	while number>0:	
		rem=number % 10
		reverse=reverse*10+rem
		number=number//10
	if(reverse==originalNumber):
		print("Palindrome")
		#return 1
	else:
		print("NOT Palindrome")
		#return 0

def main():
	number=int(input("Enter number :"))
	isPallindrome(number)

if __name__=="__main__":
	main()
