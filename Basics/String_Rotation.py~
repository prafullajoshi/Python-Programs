#Write a program to accept 2 strings from user. And check if second string is a right rotation of first string.
#Hint:
#India, iaInd -> This should be true
#Jeetendra 1st right rotation "aJeetendr"
#          2nd right rotation "raJeetend"

#!/usr/bin.python
def isRotation(string1,string2):
	string1=string1 + string1
	if string2 in string1:
		return 1
	else:
		return 0

def main():
	string1 = input("Enter 1st string :")
	string2 = input("Enter 2nd string :")
	if isRotation(string1,string2):
		print("{} is right rotation of {}".format(string2,string1))
	else:
		print("NO rotation")

if __name__=="__main__":
	main()
