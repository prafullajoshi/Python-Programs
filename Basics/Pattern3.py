#Write a program to display following patters. No. of rows.
#	A
#	AB
#	ABC
#	ABCD

def printPattern(rows):
	num=65
	for x in range(1,rows):
		for y in range(num,num+x):
			print chr(y),
		print
		
def main():
	rows=input("Enter number of rows :")
	printPattern(rows)

if __name__=="__main__":
	main()

