def fromkeys(input_dict,output_dict_values):
	result_dict={}
	if type(output_dict_values)==list or type(output_dict_values)==tuple:
		keys_list=input_dict.keys()
		values_length=len(output_dict_values)
		for i in range(len(keys_list)):
			if i < values_length:
				result_dict[keys_list[i]]=output_dict_values[i]
			else:
				result_dict[keys_list[i]]=None
	else:
		result_dict=dict.fromkeys(input_dict,output_dict_values)
	return result_dict
	
def main():
	input_dict={1:2,3:4,5:6,7:8,9:10}
	values=list(input("Enter the values to be added :"))
	fromkeys(input_dict,values)
	result_dict=fromkeys(input_dict,values)
	print("{}".format(result_dict))
	
if __name__=="__main__":
	main()
