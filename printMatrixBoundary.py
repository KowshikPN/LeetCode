def printMatrixBoundary(matrix):

	rows = len(matrix)
	cols = len(matrix[0])

	if rows == 1:
		print(matrix)
		return

	if cols == 1:
		for i in range(rows):
			for j in range(cols):
				print(matrix[i][j])
		return

	#left to right row
	i = 0
	for j in range(len(matrix)):
		print(matrix[i][j])
	print()

	#up to down col
	j = len(matrix[0]) - 1
	for i in range(1,len(matrix)):
		print(matrix[i][j])
	print()


	#right to left row
	i = len(matrix)-1
	for j in range(len(matrix)-2,-1,-1):
		print(matrix[i][j])
	print()

	#down to up col
	j = 0
	for i in range(len(matrix)-2,0,-1):
		print(matrix[i][j])
	print()


matrix = [[2,5,1],[3,7,2],[5,9,0]]
printMatrixBoundary(matrix)





'''
2 5 1
3 7 2
5 9 0
'''