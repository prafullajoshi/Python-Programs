#Write a program to accept sentence from user and print count of characters, words in the given statement
def countOfCharWords(line):
	charCount=0
	wordCount=1
	for x in range(len(line)):
		if not line[x]==" ":
			charCount+=1
		else:
			wordCount+=1
	print("Characters={}  Words={}".format(charCount,wordCount))
def main():
	line=input("Enter sentence :")
	countOfCharWords(line)
if __name__=="__main__":
	main()
		
