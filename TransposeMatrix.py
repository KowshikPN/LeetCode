def Transpose(matrix):
	tmp = [[]*len(matrix) for i in range(len(matrix[0]))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			tmp[j].append(matrix[i][j])

	print(tmp)



matrix = [[1,2,3],[4,5,6],[9,8,7]]
Transpose(matrix)