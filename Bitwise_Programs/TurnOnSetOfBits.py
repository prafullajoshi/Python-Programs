#Write a program to accept number, position and number of bits to turn ON. Turn ON the respective bits from the number and return number.
def TurnOnSetOfBits(num,pos,noOfBits):
	if pos > noOfBits:
		x=1
		x=(x<<noOfBits)-1
		x=x<<(pos-noOfBits)
		num=num | x
		return num

def main():
	num=input("Enter the number :")
	pos=input("Enter the position :")
	noOfBits=input("Enter number of bits :")
	print("After turning on {} bits from {} is :{}".format(noOfBits,num,TurnOnSetOfBits(num,pos,noOfBits)))
	
if __name__=="__main__":
	main()
