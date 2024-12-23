def matrix_vector_mult(A,b):
    """
    A:
    b:
    
    
    """
    # Check matrices can be multiplied
    if len(A[0]) != len(b):
        raise ValueError(
            f"Cannot multiply a {len(A[0])}x{len(A)} matrix "
            f"with a {len(b)}-dimensional vector. "
            f"Matrix columns must equal vector dimensions"
        )
    else:
        results = {}
        for i in range(len(A)):
            results[i] = []
        
        # iterate through each row of the matrix 
        for row in range(len(A)):
                    # iterate through each item in the vector 
                    for j in range(len(b)):
                        # run multiplication and add to result list 
                        result = A[row][j] * b[j]
                        results[row].append(result)
        
        final_out = []
        for k,v in results.items():
             x = sum(v)
             final_out.append(x)
        return np.array(final_out)


