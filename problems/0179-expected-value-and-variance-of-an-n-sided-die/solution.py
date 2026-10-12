def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	total = 0
	for x in range(1, n + 1):
		total += x
	expectation = total / n

	# expectation = (n + 1) / 2

	# Var(X) = E(X^2) - (E(X))^2
	total2 = 0
	for x in range(1, n + 1):
		total2 += x ** 2
	expectation_x_square = total2 / n

	variance = expectation_x_square - expectation ** 2

	return [expectation, variance]