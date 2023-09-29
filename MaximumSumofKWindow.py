def maximum_sum(arr,k):
	if len(arr) == 0:
		return 0

	curr_sum = 0
	global_sum  = 0

	for i in range(k):
		curr_sum += arr[i]

	for i in range(k,len(arr)):
		curr_sum += arr[i] - arr[i-k]
		global_sum = max(global_sum,curr_sum)

	return global_sum


arr = [1,8,30,-5,20,7]
k = 3
out = maximum_sum(arr,k)
print(out)