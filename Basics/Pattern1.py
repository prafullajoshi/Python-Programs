#Write a program to display following patters. No. of rows.
#	*
#	* *
#	* * *
#	* * * *

def printPattern(rows):
	for x in range(1,rows+1):
		for y in range(x):
			print ('*'),
		print

def main():
	rows=input("Enter number of rows :")
	printPattern(rows)

if __name__=="__main__":
	main()

