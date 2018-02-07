#To accept 3 numbers from user & check if those 3 numbers can result into creating a traingle. (Hint: Sum of 2 side is greater than 2 sides)

#!/usr/bin/python
def isTriangle(iSide1,iSide2,iSide3):
	if (iSide1+iSide2) > iSide3:
		return 1
	elif (iSide2+iSide3) > iSide1:
		return 1
	elif (iSide1+iSide3) > iSide2:
		return 1
	else:
		return 0
	
def main():
	iSide1=input("Enter 1st side :")
	iSide2=input("Enter 2nd side :")
	iSide3=input("Enter 3rd side :")
	if not isTriangle(iSide1,iSide2,iSide3):
		print("NOT triangle")
	else:
		print("Triangle")
		
if __name__=="__main__":
	main()
