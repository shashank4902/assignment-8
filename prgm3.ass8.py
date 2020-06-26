3#count the number of times letter "o" in the string "hello world"
test_str="hello world"
res={}
for keys in test_str:
	res[keys]=res.get(keys,0)+1
print("count of all characters in hello world is:\n"+str(res))