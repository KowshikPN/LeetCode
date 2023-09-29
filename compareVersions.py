def compare(s1,s2):
	versions1 = s1.split(".")
	versions2 = s2.split(".")

	for i in range(max(len(versions1),len(versions2))):
		v1 = int(versions1[i]) if i < len(versions1) else 0
		v2 = int(versions2[i]) if i < len(versions2) else 0
		#print(v1,v2)
		if v1 > v2:
			return "Greater"
		elif v1 <v2:
			return "Lesser"
	return "Equal"


s1 = "1"
s2 = "1.0.1"
out = compare(s1,s2)
print(out)

