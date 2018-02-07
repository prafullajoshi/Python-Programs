#Write a program to turn OFF right most bit
def TurnOffRightMostBit(num):
	x=1
	if(num!=0):
		while(x<num):
			if (num & x) ==0:
				x=x<<1
			else:
				break
	x=~x
	num=num & x
	return num
	
def main():
	num=input("Enter the number :")
	print("After Turning off right most 1 bit :{}".format(TurnOffRightMostBit(num)))
if __name__=="__main__":
	main()
