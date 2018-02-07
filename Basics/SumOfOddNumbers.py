#Write a program to accept a range from user & display sum of odd numbers in that range

#!/usr/bin/python

def getSumOfOddNumbers(iLower,iUpper):
	sum=0
	for x in range(iLower,iUpper,1):
		if(x & 1):
			sum=sum+x
	return sum

def main():
	iLower=input("Enter lower bound :")
	iUpper=input("Enter upper bound :")
	print("Sum of odd numbers in given range :{}".format(getSumOfOddNumbers(iLower,iUpper)))

if __name__=="__main__":
	main()
