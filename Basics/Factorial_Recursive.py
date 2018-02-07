#Write a recursive function which accept a number from user and print its factorial
def getFactorial(num):
	if num==0:
		return 1
	else:
		return num*getFactorial(num-1)

def main():
	num=input("Enter number :")
	print("Factorial of {} is {}".format(num,getFactorial(num)))
if __name__=="__main__":
	main()
