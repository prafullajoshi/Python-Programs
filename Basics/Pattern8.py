#Write a program to display following patters. No. of rows.
#		*
#	  * * *
#	* * * * *
# * * * * *	* *
#	* * * * *
#	  * * *
#		*
def printPattern(rows):
	for i in range(1,rows+1):
		for j in range(rows-i):
			print(" "),
		for j in range((2*i)-1):
			print("*"),
		print
	for i in range(1,rows):	
		for j in range(i):
			print(" "),
		for j in range(2*(rows-1)-i,i+1,-1):
		#for j in range(rows-i):
			print("*"),
		print
def main():
	rows=input("Enter number of rows :")
	printPattern(rows)
if __name__=="__main__":
	main()
