#Write a program to accept a number from user and count number of 1 bits in the given number
def CountOfOneBits(num):
	x=1
	count=0
	while x<=num:
		if num & x!=0:
			count+=1
		x=x<<1
	return count
def main():
	num=input("Enter the number :")
	print("Count of 1 bits in {} is :{}".format(num,CountOfOneBits(num)))
if __name__=="__main__":
	main()		
