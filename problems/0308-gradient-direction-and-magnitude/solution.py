import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = np.linalg.norm(gradient)

	if magnitude == 0:
		direction = [0] * len(gradient)
	else :
		direction = [x / magnitude for x in gradient]
	descent_direction = [- x for x in direction]
	res = dict()
	res["magnitude"] = magnitude
	res["direction"] = direction
	res["descent_direction"] = descent_direction
	return res 