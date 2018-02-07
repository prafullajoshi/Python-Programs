#Write a function which should be able to add 2 numbers,3 numbers,4 numbers or 5 numbers

#!/usr/bin/python
def add(a,b=0,c=0,d=0,e=0):
	return (a+b+c+d+e)
def main():
	print("Addition :{}".format(add(12,13)))
	print("Addition :{}".format(add(12,13,4)))
	print("Addition :{}".format(add(12,13,23,14)))
	print("Addition :{}".format(add(12,13,3,45,11)))
if __name__=="__main__":
	main()
