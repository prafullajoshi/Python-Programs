#Write a program to display following patters. No. of rows.
#	* * * * * * * 
#	  * * * * *
#		* * * 
# 		  *

def printPattern(rows):
	for i in range(1,rows+1):
		for j in range(i):
			print(" "),
		##if not i % 2 == 0:
		#for j in range((2*rows)-(i+2)):
		#k=1
		for j in range(2*rows-i):
			print("*"),
			#k+=2
		print
def main():
	rows=input("Enter number of rows :")
	printPattern(rows)
if __name__=="__main__":
	main()
