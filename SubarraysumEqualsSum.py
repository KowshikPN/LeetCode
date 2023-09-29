'''
Check if the subarray_sum equals the given sum

'''
def check(arr,sums):
	i = 0
	j = 0
	while j <= len(arr):
		if arr[i] == sums:
			return True

		if sum(arr[i:j+1]) == sums:
			return True
		elif sum(arr[i:j+1]) < sums:
			j += 1
		else:
			i += 1

	return False


arr = [1,4,20,3,10,5]
given_sum = 33
out = check(arr,given_sum)
print(out)

