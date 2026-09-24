def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	total = 0
	if mode == "row":
		for i in range(len(matrix)):
			total = 0
			for j in range(len(matrix[0])):
				total += matrix[i][j]
			means.append(total / len(matrix[0]))
	else:
		for j in range(len(matrix[0])):
			total = 0
			for i in range(len(matrix)):
				total += matrix[i][j]
			means.append(total / len(matrix))
	return means