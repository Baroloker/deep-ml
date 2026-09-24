import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	# arr = np.array(a)
	# if arr.size != new_shape[0] * new_shape[1]:
	# 	return []
	# reshaped_matrix = np.reshape(arr, new_shape).tolist()

	flat = []
	for i in range(len(a)):
		for j in range(len(a[0])):
			flat.append(a[i][j])
	
	if len(flat) != new_shape[0] * new_shape[1]:
		return []

	reshaped_matrix = []
	for i in range(new_shape[0]):
		tmp = []
		for j in range(new_shape[1]):
			tmp.append(flat[i * new_shape[1] + j])
		
		reshaped_matrix.append(tmp)

	return reshaped_matrix