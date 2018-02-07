# Write a program to accept 2 numbers and print minimum of them

#!/usr/bin/python
def getMin(iNum1,iNum2):
	if iNum1!=iNum2:
		if iNum1<iNum2:
			return iNum1
		else:
			return iNum2

def main():
	iNum1=input("Enter 1st number :")
	iNum2=input("Enter 2nd number :")
	print("Minimum number is :{}".format(getMin(iNum1,iNum2)))

if __name__=="__main__":
	main()
