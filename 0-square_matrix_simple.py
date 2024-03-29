#usr/bin/python3
def square_matrix_simple(matrix=[]):
    """compute the square of all integers in the matrix"""
    if not matrix:
        return None

    return list(list(map(lambda a: a*a, num_list)) for num_list in matrix)
