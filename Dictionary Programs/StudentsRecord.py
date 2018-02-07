'''Write a program to accept student record from user and store it in dictiornary. Roll_No should be auto-generated. Make dictionary of dictionary as following :

		Student{1:{"name":"prafulla","DOB":"21-10-94"}
				2:{"name":"jeetendra","DOB":"29-12-86"}
			   }
'''
import sys

roll_no = 0

def insertStudent(student_dict,result_dict):
	student_dict={}
	name = input("Enter name :")
	dob = input("Enter date of birth :")
	marks = input("Enter marks :")
	
	student_dict["name"] = name
	student_dict["dob"] = dob
	student_dict["marks"] = marks

	
	
	return createStudent(student_dict,result_dict,name,dob,marks)
	
def createStudent(student_dict,result_dict,name,dob,marks):
	
		
	global roll_no
	roll_no+=1
	result_dict[roll_no] = student_dict

	print(result_dict)
	return result_dict

def searchRecord(student_dict_final):
	roll=input("Enter roll number to search :")
	if student_dict_final.has_key(roll):
		print(student_dict_final[roll])

def updateRecord(student_dict_final):
	roll = input("Enter roll number to update marks of :")
	if student_dict_final.has_key(roll):
		updated_marks = input("Enter new marks :")
		student_dict_final[roll][] = updated_marks
		print("Marks updated successfully..!")
		print(student_dict_final[roll])
	else:
		print("Roll number does not exist")
	
		
def menu():
	print("1.Insert Student Record\n2.Display Record\n3.Update\n4.Search Record\n5.Exit\n")
	choice = input("Enter the choice :")
	return choice
	
def simulateMain():
	student_dict={}
	result_dict={}
	student_dict_final={}
	choice = menu()
	while choice != 5:
		if choice == 1:
			student_dict_final=insertStudent(student_dict,result_dict)
		elif choice == 2:
			print("in choice 2")	
		elif choice == 3:
			print("in choice 3")
			updateRecord(student_dict_final)
		elif choice == 4:
			print("in choice 4")
			searchRecord(student_dict_final)
		elif choice == 5:
			sys.exit()
		else:
			print("Invalid choice..!!")
		choice=menu()

def main():
	simulateMain()

if __name__=="__main__":
	main()	
