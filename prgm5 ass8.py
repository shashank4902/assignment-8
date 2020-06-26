5#substring in a string
teststr="hello world"
count=0
for i in teststr:
	if i=='l':
		count=count+1
print("count of l in hello world is:"+str(count))