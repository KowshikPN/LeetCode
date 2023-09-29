def generate_substrings(s,res):
	for i in range(len(s)):
		for j in range(i+1,len(s)+1):
			res.append(s[i:j])


def even_substrings(res):
	one_count = 0
	zero_count = 0
	final_count = 0
	for ele in res:
		for val in ele:
			if int(val) == 0:
				zero_count += 1
			else:
				one_count += 1

		if zero_count == one_count:
			final_count += 1

	return final_count


s = "1010110"
res = []
generate_substrings(s,res)
#print(res)
output = even_substrings(res)
print(output)

