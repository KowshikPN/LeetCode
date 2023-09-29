s1 = "<hello> <world>\\"
res = []
for ele in s1:
	res.append(ele)
for i in range(len(res)):
	if res[i] == "<":
		res[i] = "\<"
	elif res[i] == ">":
		res[i] = "\>"
	elif res[i] == "\\":
		continue
	
s1 = "".join(res)
print(s1)
