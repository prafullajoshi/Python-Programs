def VariableNumberOfArguemtns(*args):
	print(type(args))
	for x in args:
		print(x)
def main():
	VariableNumberOfArguemtns(1,2,3,4)
	VariableNumberOfArguemtns(4,5,7,11,15,"hi","Bye")
if __name__=='__main__':
	main()
