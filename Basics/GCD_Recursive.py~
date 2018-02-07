#Write a recursive function for GCD
def getGCD(num1,num2):
	if num1==num2:
		return num1
	elif num1 > num2:
		return getGCD(num1-num2,num2)
	else:
		return getGCD(num1,num2-num1)

def main():
	num1=input("Enter 1st number :")
	num2=input("Enter 2nd number :")
	result=getGCD(num1,num2)
	print("GCD of {} and {} is {}".format(num1,num2,result))
if __name__=="__main__":
	main()
