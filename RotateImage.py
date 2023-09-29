def rotateImage(matrix):
	tmp = [[]*len(matrix) for i in range(len(matrix))]
	count = 0
	while count != len(matrix):
		j = len(matrix)-1
		for i in range(len(matrix)):
			tmp[count].append(matrix[i][j])
		count += 1


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateImage(matrix)