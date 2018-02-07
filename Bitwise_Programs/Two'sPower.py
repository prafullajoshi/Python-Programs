#Write a program to check whether the given number is 2's power or not

def isTwosPower(num):
	return num & (num-1)==0
def main():
	num=input("Enter the number :")
	if(isTwosPower(num)):
		print("{} is 2's power".format(num))
	else:
		print("{} is NOT 2's power".format(num))
	
if __name__=="__main__":
	main()		
