#Write a program to display following patters. No. of rows.
#		 A
#      B A B
#	 C B A B C
#  D C B A B C D
def printPattern(rows):
	num=64
	for i in range(1,rows+1):
		for j in range(rows-i):
			print(" "),
		for j in range(num+i,num,-1):
			print chr(num),
		print
def main():
	rows=input("Enter number of rows :")
	printPattern(rows)
if __name__=="__main__":
	main()

