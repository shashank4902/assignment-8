7#deletion of a character
def remove(string,i):
	a=string[:i]
	b=string[i+1:]
	return a+b
if __name__==" __main__":
	string="helloworld"
	i=5
	print(remove(string,i))