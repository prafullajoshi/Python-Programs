#Write a program to display following patters. No. of rows.
#	* * * *
#	* * *
#	* *
#	*

def printPattern(rows):
	for i in range(1,rows+1):
		for j in range(i,rows+1):
			print ('*'),
		print

def main():
	rows=input("Enter number of rows :")
	printPattern(rows)

if __name__=="__main__":
	main()

