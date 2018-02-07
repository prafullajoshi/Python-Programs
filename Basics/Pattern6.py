#Write a program to display following patters. No. of rows.
#		*
#	  * * *
#	* * * * *
# * * * * *	* *

def printPattern(rows):
	for i in range(1,rows+1):
		for j in range(rows-i):
			print(" "),
		for j in range((2*i)-1):
			print("*"),
		print

def main():
	rows=input("Enter rows :")
	printPattern(rows)

if __name__=="__main__":
	main()
