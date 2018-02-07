#Write a program to accept two lists from user and, sort hem without using built in method and merge two sorted lists

def sort(l1):
	for i in range(0,len(l1)):
		for j in range(i+1,len(l1)):
			if l1[i] > l1[j]:
				temp = l1[i]
				l1[i] = l1[j]
				l1[j] = temp
	return l1

def Merge(l1,l2):
	l3=[]
	i=0
	j=0
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if i < len(l1):
		l3.extend(l1[i:])
	if j < len(l2):
		l3.extend(l2[j:])
	return l3		
def main():
	l1=[]
	l2=[]
	l1=input("Enter first list :")
	l2=input("Enter second list :")

	print("After sorting :")
	l1=sort(l1)
	l2=sort(l2)
	l3=Merge(l1,l2)
	print(l1)
	print(l2)
	print("After merging sorted lists :")
	print(l3)
	
if __name__=="__main__":
	main()
