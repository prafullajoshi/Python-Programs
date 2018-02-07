
def readConfigFile(line):
	#fd = open(input_file)
	value
	result = {}
	#line = fd.readline()
	while line!="":
		if not line.startswith("#") and "=" in line:
			l1 = line.split("=")				# list['HFP','True']
			value = l1[1]
			if "#" in l1[1]:
				value = l1[1].split("#")[0]
		result[l1[0]] = value[:-1]
		line = fd.readline()
	#print(result)
	print("in readfile")
	return result

def dictOfdict(input_file):
	print("in start of func")
	fd=open(input_file)
	line = fd.readline()
	final_dict={}
	while line!="":
		print("in while")
		if line.startswith("["): 
			print("in if")
			value1=line[1:-1]
			final_dict[value1]=readConfigFile(line)
		line = fd.readline()		
	print(final_dict)
	print("in dictOfdict")
def main():
	input_file=input("Enter file name :")
	dictOfdict(input_file)


if __name__=="__main__":
	main()		
