#Write a program to accept a range from user and display all the numbers in that range which are not multiple of two and three
def getNumbersInRange(iLower,iUpper):
	for i in range(iLower,iUpper+1):
		if i%2==0 or i%3 ==0:
			continue
		print(i)
def main():
	iLower=input("Enter lower bound :")
	iUpper=input("Enter upper bound :")
	getNumbersInRange(iLower,iUpper)
if __name__=="__main__":
	main()
