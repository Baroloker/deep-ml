from math import sqrt

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	trace = a + d
	det = a * d - b * c

	eigenvalues = []
	eigenvalues.append((trace + sqrt(trace ** 2 - 4 * det)) / 2)
	eigenvalues.append((trace - sqrt(trace ** 2 - 4 * det)) / 2)
	return eigenvalues