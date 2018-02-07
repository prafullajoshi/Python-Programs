#Write a program to accept a number from user and count number of 0 bits in the given number
def CountOfZeroBits(num):
	x=1
	count=0
	while x<=num:
		if num & x!=1:
			count+=1
		x=x<<1
	return count
def main():
	num=input("Enter the number :")
	print("Count of 0 bits in {} is :{}".format(num,CountOfZeroBits(num)))
if __name__=="__main__":
	main()		
