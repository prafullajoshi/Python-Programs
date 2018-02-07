#Accept 3 numbers, and write OPTIMIZED program to find out minimum number. Print minimum numbers

#!/usr/bin/python
def getMinOfThree(iNum1,iNum2,iNum3):
	if iNum1<iNum2:
		iNum2=iNum1
	if iNum2<iNum3:
		return iNum2
	else:
		return iNum3
def main():
	iNum1=input("Enter 1st number :")
	iNum2=input("Enter 2nd number :")
	iNum3=input("Enter 3rd number :")
	print("Minimum of 3 numbers is :{}".format(getMinOfThree(iNum1,iNum2,iNum3)))

if __name__=="__main__":
	main()
