6#compare two strings
if __name__=="__main__":
	string1=input("enter the first string:")
	print(string1,end="\n ")
	string2=input("enter the second string:")
	print(string2,end="\n")
	print("are both strings are same:",end=" ")
	if(string1==string2):
		print("yes")
	else:
		print("no")
	