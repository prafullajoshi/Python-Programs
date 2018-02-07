#Write a program to accept number, position and number of bits to turn off. Turn off the respective bits from the number and return number.
def TurnOffSetOfBits(num,pos,noOfBits):
	if pos > noOfBits:
		x=1
		x=(x<<noOfBits)-1
		x=x<<(pos-noOfBits)
		x=~x
		num=num & x
		return num

def main():
	num=input("Enter the number :")
	pos=input("Enter the position :")
	noOfBits=input("Enter number of bits :")
	print("After turning off {} bits from {} is :{}".format(noOfBits,num,TurnOffSetOfBits(num,pos,noOfBits)))
	
if __name__=="__main__":
	main()
