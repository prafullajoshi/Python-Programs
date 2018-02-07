#Write a program to accept string as :aabbcccddabbb and output: a2b2c3d2a1b3

def countChar(string):
	count=0
	i=0
	result_string=""
	while i < len(string):
		char_to_check=string[i]
		count=1
		while(i+1 < len(string) and string[i+1]==char_to_check):
			count+=1
			i+=1
		result_string+=char_to_check+str(count)
		i+=1
	return result_string


def main():
	string=input("Enter string :")
	result_string=countChar(string)
	print("{}".format(result_string))

if __name__=="__main__":
	main()
