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
    for _, row in enumerate(matrix_a):
        # iterate through each item in the vector
        for _, j in enumerate(vector_b):
            # run multiplication and add to result list
            result = matrix_a[row][j] * vector_b[j]
            results[row].append(result)

    final_out = []
    for _, v in results.items():
        x = sum(v)
        final_out.append(x)
    return np.array(final_out)


def matrix_matrix_mult(matrix_a: int, matrix_b: int):
    """
    Function 
    matrix_a

    matrix_b


    """
    pass


def main():
    """
    Main function

    """
    matrix = [[0, 1, 5, 12, 9],
              [1, 1, 5, 5, 9],
              [1, 3, 5, 6, 9]]

    vector = [0, 1, 2, 6, 6]

    answer = matrix_vector_mult(matrix_a=matrix, vector_b=vector)
    print(answer)
    return answer


if __name__ == "__main__":
    main()
