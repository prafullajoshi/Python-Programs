#Menu-driven program for all bitwise operations
import sys
def TurnOffSetOfBits(num,pos,noOfBits):
	if pos > noOfBits:
		x=1
		x=(x<<noOfBits)-1
		x=x<<(pos-noOfBits)
		x=~x
		num=num & x
		return num
	
def TurnOnSetOfBits(num,pos,noOfBits):
	if pos > noOfBits:
		x=1
		x=(x<<noOfBits)-1
		x=x<<(pos-noOfBits)
		num=num | x
		return num

def ToggleSetOfBits(num,pos,noOfBits):
	if pos > noOfBits:
		x=1
		x=(x<<noOfBits)-1
		x=x<<(pos-noOfBits)
		#x=~x
		num=num ^ x
		return num

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

def SwapSetOfBitsWithDifferentPositions(num1,num2,pos1,pos2,noOfBits):
	temp=1
	temp=(temp<<noOfBits)-1
	temp1=temp<<(pos1-noOfBits)
	temp2=temp<<(pos2-noOfBits)
	

	x_part=(num1 & temp1) >> (pos1-noOfBits)
	y_part=(num2 & temp2) >> (pos2-noOfBits)
	
	x_part=x_part << (pos2-noOfBits)
	y_part=y_part << (pos1-noOfBits)
		
	num1=num1 & (~temp1)
	num2=num2 & (~temp2)
		
	x_swapped=y_part | num1
	y_swapped=x_part | num2	
	return x_swapped,y_swapped

def CountOfOneBits(num):
	x=1
	count=0
	while x<=num:
		if (num & x)!=0:
			count+=1
		x=x<<1
	return count

def CountOfZeroBits(num):
	x=1
	count=0
	while x<=num:
		if (num & x)==0:
			count+=1
		x=x<<1
	return count

def isMultipleOfEight(num):
	if num & 7==0:
		return 1
	else:
		return 0

def isMultipleOf32(num):
	if num & 31==0:
		return 1
	else:
		return 0

def isTwosPower(num):
	return num & (num-1)==0
	
def Menu():
	print("*****************************************************************")
	print("+++BITWISE OPERATIONS+++")
	print("1.Turn OFF set of bits\n2.Turn ON set of bits\n3.Toggle set of bits\n4.Turn OFF right most bit\n5.Swap set of bits\n6.Swap set of bits with different positions\n7.Count of 1 bits\n8.Count of 0 bits\n9.Multiple of 8\n10.Multiple of 32\n11.Two's power\n12.Exit\n")
	choice=input("Enter your choice :")
	return choice

def SimulateMain():
	choice=Menu()
	while(1):
		if choice == 1:
			num=input("Enter the number :")
			pos=input("Enter the position :")
			noOfBits=input("Enter number of bits to turn OFF :")
			print("After turning OFF {} bits from {} is :{}".format(noOfBits,num,TurnOffSetOfBits(num,pos,noOfBits)))	
		
		elif choice == 2:
			num=input("Enter the number :")
			pos=input("Enter the position :")
			noOfBits=input("Enter number of bits to turn ON :")
			print("After turning ON {} bits from {} is :{}".format(noOfBits,num,TurnOnSetOfBits(num,pos,noOfBits)))
		
		elif choice == 3:
			num=input("Enter the number :")
			pos=input("Enter the position :")
			noOfBits=input("Enter number of bits to toggle :")
			print("After toggling {} bits from {} is :{}".format(noOfBits,num,ToggleSetOfBits(num,pos,noOfBits)))
		
		elif choice == 4:
			num=input("Enter the number :")
			print("After Turning off right most 1 bit :{}".format(TurnOffRightMostBit(num)))
		
		elif choice == 5:
			num1=input("Enter 1st number :")
			num2=input("Enter 2nd number :")
			pos=input("Enter the position :")
			noOfBits=input("Enter number of bits :")
			if pos > noOfBits:
				x_swapped,y_swapped=SwapSetOfBits(num1,num2,pos,noOfBits)
				print("After swapping {} bits from {}  and {} \n".format(noOfBits,num1,num2,SwapSetOfBits(num1,num2,pos,noOfBits)))
				print("x_swapped :{}\ny_swaped :{}".format(x_swapped,y_swapped))
			else:
				print("Position must be larger than number of bits to be swapped.\nExiting..")
		
		elif choice == 6:
			num1=input("Enter 1st number :")
			pos1=input("Enter the position for 1st number :")
	
			num2=input("Enter 2nd number :")
			pos2=input("Enter the position for 2nd number :")
			noOfBits=input("Enter number of bits to swap :")
	
			if pos1 > noOfBits and pos2 > noOfBits:
				x_swapped,y_swapped=SwapSetOfBitsWithDifferentPositions(num1,num2,pos1,pos2,noOfBits)
				print("After swapping {} bits from {}  and {} with different position ".format(noOfBits,num1,num2))
				print("x_swapped :{}\ny_swaped :{}".format(x_swapped,y_swapped))
			else:
				print("Position must be larger than number of bits to be swapped.\nExiting..")
	
		elif choice == 7:
			num=input("Enter the number :")
			print("Count of 1 bits in {} is :{}".format(num,CountOfOneBits(num)))
		
		elif choice == 8:
			num=input("Enter the number :")
			print("Count of 0 bits in {} is :{}".format(num,CountOfZeroBits(num)))
		
		elif choice == 9:
			num=input("Enter the number :")
			if isMultipleOfEight(num)==1:
				print("{} is multiple of 8".format(num))
			else:
				print("{} is NOT multiple of 8".format(num))
		
		elif choice == 10:
			num=input("Enter the number :")
			if isMultipleOf32(num)==1:
				print("{} is multiple of 32".format(num))
			else:
				print("{} is NOT multiple of 32".format(num))
		
		elif choice == 11:
			num=input("Enter the number :")
			if(isTwosPower(num)):
				print("{} is 2's power".format(num))
			else:
				print("{} is NOT 2's power".format(num))
		
		elif choice == 12:
			sys.exit()
		
		else:
			print("You entered invalid choice.")	
		choice=Menu()

def main():
	SimulateMain()

if __name__=="__main__":
	main()
