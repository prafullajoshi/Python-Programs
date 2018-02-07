#Write a program to accept a number from user and check if it is multiple of 8 or not without using any arithmetic operator
def isMultipleOfEight(num):
	if num & 7==0:
		return 1
	else:
		return 0
def main():
	num=input("Enter the number :")
	if isMultipleOfEight(num)==1:
		print("{} is multiple of 8".format(num))
	else:
		print("{} is NOT multiple of 8".format(num))
if __name__=="__main__":
	main()		
