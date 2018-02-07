#Write a program to perform menu driven arithmatic operations. Hind: write funt for + - * /. Show choices to user +-*/exit.

#!usr/bin/python
import sys
def add(no1,no2):
    return no1+no2
    
def sub(no1,no2):
    return no1-no2
    
def mul(no1,no2):
    return no1*no2
    
def div(no1,no2):
    return no1/no2

def acceptNumbers():
	iNum1=input("Enter 1st number :")
	iNum2=input("Enter 2nd number :")
	
def menu():
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=input("Enter your choice :")
    return choice
while True:
    choice=menu()
    if choice==1:
		acceptNumbers()
		print("Addition of {} and {} is :{}".format(iNum1,iNum2,add(iNum1,iNum2)))
	elif choice==2:
		acceptNumbers()
        result=sub(iNum1,iNum2)
        print("Subtraction of {} and {} is :{}".format(iNum1,iNum2,sub(iNum1,iNum2)))
    elif choice==3:
    	acceptNumbers()
        result=mul(iNum1,iNum2)
        print("Multiplication of {} and {} is :{}".format(iNum1,iNum2,mul(iNum1,iNum2)))
    elif choice==4:
    	acceptNumbers()
        result=div(iNum1,iNum2)
        print("Division of {} and {} is :{}".format(iNum1,iNum2,div(iNum1,iNum2)))
	elif choice==5:
		sys.exit(0)
	else:
		print("Invalid choice..exiting")
    	sys.exit(0)

def main():
	menu()

if __name__=="__main__":
	main()
