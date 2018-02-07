#Write a program to accept n numbers from user and display addition of them
def sumOfNumbers(array):
	addition=0
	for i in array:
		addition+=array[i]
	print("Sum of given numbers={}".format(addition))
def main():
	count=input("How many numbers :")
	array=[count+1]
	for x in range(0,count):
		array[x]=input("Enter number :")
	sumOfNumbers(array)
if __name__=="__main__":
	main()
