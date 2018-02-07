#Write a program to accept a number from user and check if it is amstrong or not
def isAmstrongNumber(number):
	num=number
	digit=0
	cube=0
	sum1=0
	while num!=0:
		digit=num%10
		cube=digit*digit*digit
		sum1+=cube
		num=num//10
	if sum1 == number:
		return 1
	else:
		return 0
def main():
	number=input("Enter number :")
	if isAmstrongNumber(number):
		print("Amstrong number")
	else:
		print("NOT amstrong number")
if __name__=="__main__":
	main()
