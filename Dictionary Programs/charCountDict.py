#Write a program to accept a string from user

def charCountDict(input_str):
	result_dict={}
	i=0
	while i < len(input_str):
		if result_dict.has_key(input_str[i]):
			result_dict[input_str[i]] = result_dict[input_str[i]] + 1
		else:
			result_dict[input_str[i]] = 1
		i+=1
	return result_dict

def main():
	string=input("Enter string :")
	result_dict=charCountDict(string)
	print("{}".format(result_dict))

if __name__=="__main__":
	main()
		
		
