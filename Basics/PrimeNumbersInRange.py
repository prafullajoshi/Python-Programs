#Write a program to accept a range from user & display prime numbers from that range

#!/usr/bin/python
def printPrimeNumbers(iLower,iUpper):
	for x in range(iLower,iUpper+1):
		if x>1:
			for y in range(2,x):
				if x % y == 0:
					break
			else:
				print(x )
		else:
			print("Invalid input range")
		
def main():
	iLower = input("Enter lower bound :")
	iUpper = input("Enter upper bound :")
	printPrimeNumbers(iLower,iUpper)
	
if __name__=="__main__":
	main()
