def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    transposed_a = []
    for j in range(len(a[0])):
        tmp = []
        for i in range(len(a)):
            tmp.append(a[i][j])
        transposed_a.append(tmp)
    return transposed_a

    
    
    