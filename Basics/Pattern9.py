#Write a program to print the following pattern
#	2
#	3  5
#	7  11  13
#	17 19  23 29

def primeNumber(num):
	flag=1
	for i in range(2,num):
		if num % i ==0:
			flag=0
			break
	if flag==1: 
		return 1
	else:
		return 0

def printPattern(rows):
	num=2
	for i in range(1,rows+1):
		for j in range(i):
			while not primeNumber(num):
				num=num+1
			print(num),
			num+=1
		print

def main():
	rows=input("\nEnter the number of rows :")
	printPattern(rows)

if __name__=="__main__":
	main()
