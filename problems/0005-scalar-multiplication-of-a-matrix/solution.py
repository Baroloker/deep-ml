def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = matrix
	for i in range(len(result)):
		for j in range(len(result[0])):
			result[i][j] = result[i][j] * scalar
	
	return result
	