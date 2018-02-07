#Write a program to accept two numbers from user,accept position and no of bits to be swapped from given two numbers
def SwapSetOfBits(num1,num2,pos,noOfBits):
	temp=1
	temp=(temp<<noOfBits)-1
	temp=temp<<(pos-noOfBits)

	x_part=num1 & temp
	y_part=num2 & temp
		
	num1=num1 & (~temp)
	num2=num2 & (~temp)
		
	x_swapped=y_part | num1
	y_swapped=x_part | num2	
	return x_swapped,y_swapped

def main():
	num1=input("Enter 1st number :")
	num2=input("Enter 2nd number :")
	pos2=input("Enter the position :")
	noOfBits=input("Enter number of bits to swap :")
	
	if pos1 > noOfBits:
		x_swapped,y_swapped=SwapSetOfBits(num1,num2,pos,noOfBits)
		print("After swapping {} bits from {}  and {} \n".format(noOfBits,num1,num2,SwapSetOfBits(num1,num2,pos,noOfBits)))
		print("x_swapped :{}\ny_swaped :{}".format(x_swapped,y_swapped))
	else:
		print("Position must be larger than number of bits to be swapped.\nExiting..")
	
if __name__=="__main__":
	main()
