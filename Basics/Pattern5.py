#Write a program to display following patters. No. of rows.
#	* * * *
#	  * * *
#		* *
#  		  *

def printPattern(rows):
	for i in range(0,rows):
		for j in range(i):
			print(" "),
		for j in range(rows-i):
			print("*"),
		print
def main():
	rows=input("Enter the number of rows :")
	printPattern(rows)

if __name__=="__main__":
	main()
