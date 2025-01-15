# linear-algebra

 

##

 

## 2. Matrix Determinant 

 

We calculate the determinant using Lower-Upper ddecomposition. Here, we split the input matrix, A, into two matrices such that, A = LU.

 

A = | 4  1  3 |

    | 3  0  1 |

    | 4  5  3 |

 

L is the lower triangle of the matrix with all diagonal entries are equal to 1.
 

L = | 1  *  * |

    | 3  1  * |

    | 4  5  1 |
   
U is the upper triangle as so:

U = | 4  1  3 |

    | *  0  1 |

    | *  *  3 |