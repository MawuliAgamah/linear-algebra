"""
Functions to implement matrix operations:
1. Matrix-vector multiplication
2. Matrix addition and subtraction
3. Scalar multiplication
4. Matrix transposition
5. Determinant calculation
"""

from typing import List
import numpy as np


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols


def create_output_matrix(matrix_a: List[List[int]], matrix_b: List[List[int]]):
    """
    Creates an output matrix
    """
    rows = len(matrix_a)
    n_cols = len(matrix_b)

    results_matrix = []
    results_matrix = [[0]*n_cols for _ in range(rows)]
    return results_matrix


def matrix_vector_mult(matrix_a: List[List[int]], vector_b: List[int]):
    """
    Multiplies a matrix with a vector and returns the resulting vector.

    parameters:
    -----------
    matrix_a : list of lists or 2D array
        The input matrix to be multiplied with the vector.
        It should be of size (m, n).

    vector_b : list or 1D array
        The input vector to be multiplied with the matrix.
        of size (n,) where n is number of columns in the matrix.

    Returns
    --------
    np.ndarray:
        A 1D NumPy array representing the result of multiplying the matrix
        with the vector output will have the size (m,).

    Raises:
    ValueError
        If the number of columns in the matrix does not match
        the number of elements in the vector.

    Example:
    >>> matrix_a = [[1, 2], [3, 4], [5, 6]]
    >>> vector_b = [7, 8]
    >>> matrix_vector_mult(matrix_a, vector_b)
    array([23, 53, 83])
    """
    #  Check matrices can be multiplied
    if len(matrix_a[0]) != len(vector_b):
        raise ValueError(
            f"Cannot multiply a {len(matrix_a[0])}x{len(matrix_a)} matrix "
            f"with a {len(vector_b)}-dimensional vector. "
            f"Matrix columns must equal vector dimensions"
        )

    # pre-populate results dictionairy to
    # so output matrix is correct shape.
    results = {}
    for i in range(len(matrix_a)):
        results[i] = []

    # iterate through each row of the matrix
    for i, _ in enumerate(matrix_a):
        # iterate through each item in the vector
        for j, _ in enumerate(vector_b):
            # run multiplication and add to result list
            result = matrix_a[i][j] * vector_b[j]
            results[i].append(result)

    final_out = []
    for _, v in results.items():
        x = sum(v)
        final_out.append(x)
    return np.array(final_out)


def matrix_add_subtract(matrix_a: List[List[int]],
                        matrix_b: List[List[int]],
                        operation: str = 'add'
                        ):
    """
    matrix_a
    matrix_b
    """

    # create zeroed matrix to populate
    results_matrix = create_output_matrix(matrix_a, matrix_b)
    for idx, i in enumerate(matrix_a):
        for idx_r, _ in enumerate(i):
            if operation == 'add':
                results_matrix[idx][idx_r] = matrix_a[idx][idx_r] + \
                    matrix_b[idx][idx_r]
            else:
                results_matrix[idx][idx_r] = matrix_a[idx][idx_r] - \
                    matrix_b[idx][idx_r]

    return results_matrix


# def matrix_matrix_mult(matrix_a: int, matrix_b: int):
#    """
#    matrix_a
#    Function
#
#    matrix_b
#
#
#    """
#
#    for i, _ in enumerate(matrix_a):
#        for j, _ in enumerate(matrix_b):
#
#   return


def main():
    """
    Main function
    """
    matrix = [[0, 1, 5, 12, 9],
              [1, 1, 5, 5, 9],
              [1, 3, 5, 6, 9]]

    vector = [0, 1, 2, 6, 6]

    #  my implementation
    print('1 : matrix vector multiplication')
    print(f'{matrix}', '\n * \n', f'{vector} \n')

    answer = matrix_vector_mult(matrix_a=matrix, vector_b=vector)
    #  numpy implementation
    check = np.array(matrix).dot(np.array(vector))
    print('result :', answer)
    print('validate :', np.equal(check, answer))


if __name__ == "__main__":
    main()
