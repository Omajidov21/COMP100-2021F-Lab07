## Quiz 3

Note that this is a follow-up to the Quiz 1 that we had in the class, the solution of the Quiz 1 is given in "quiz.py". 
All you need to do in this quiz is to modify the `TO-DO` parts in the code to use exceptions and assertions to catch errors as we learned in the class.

1. Write a function `input_matrix()` that when called, asks a user to enter four floating-point numbers representing a 2x2 square matrix in row order, i.e. if the entered numbers are a, b, c, and d, then they represent this matrix:

```
M = [ a, b
      c, d ]
```

Prompt and warn the user with the appropriate exception until they enter four valid floats.

The function must return the matrix as a tuple with four elemetns in row order:

`(a, b, c, d)`

2. Write a function `inverse(M)` that takes a 2x2 matrix as a tuple with 4 elements in row order as input, and returns its inverse.

You can compute the determinant of the matrix `|M|` and its inverse `M_inv` as follows: 

```
|M| = a*d - b*c

M_inv = (1/|M|) * [ d, -b
                   -c, a ]
```
Then, return the result as a tuple with four elements in row order: 

`(d/|M|, -b/|M|, -c/|M|, a/|M|)`

In your your code, catch the cases where the determinant is 0 and raise an exception with the following error message:

> "Determinant is 0, the inverse does not exist."

** Note that in the `inverse(M)` function, you must not use any `if` statements. (use exceptions).**



3. Write a function `matmul(M1, M2)` to implement the matrix multiplication operation for 2x2 matrices by assuming that a matrix is represented as a tuple with four elements in row order, e.g. 

`M = (a, b, c, d)` to represent 

```
M = [ a, b
      c, d ]
```

Given `M1 = (a1, b1, c1, d1)` and `M2 = (a2, b2, c2, d2)`, implement the `matmul` function to return a new tuple with four elements representing the result of the matrix multiplication operation:

```
M1 x M2 = [ a1, b1   x [ a2, b2
            c1, d1 ]     c2, d2 ]
        
        = [ a1*a2+b1*c2, a1*b2+b1*d2
            c1*a2+d1*c2, c1*b2+d1*d2 ]
    

matmul(M1, M2) = (a1*a2+b1*c2, a1*b2+b1*d2, c1*a2+d1*c2, c1*b2+d1*d2) 
```

4. In this part, we want to verify that the inverse matrix computed in the second question, `M_inv`, is indeed the inverse of `M` by multiplying the two matrices and asserting that the result is approximately equal to the 2x2 identity matrix I:

```
M x M_inv ≈ I = [ 1, 0
                  0, 1 ]

matmul(M, M_inv) ≈ (1, 0, 0, 1)
```

Write a function `almost_identity(M, epsilon)` that takes a 2x2 matrix `M` as a tuple in row order form, and a small positive number `epsilon`. It checks the absolute difference between each element of the matrix `M` with the corresponding element of the identity matrix. If any of the absolute differences is greater than epsilon, it should print an error message using an `assert` statement:

> "This matrix is not equal to the identiy matrix."

otherwise it should print:

> "This matrix is approximately equal to the identiy matrix."


Note that the matrix `M = (a, b, c, d)` is approximately equal to the identiy matrix if the following conditions are met:

```
|a-1| < epsilon and |b| < epsilon and |c| < epsilon and |d-1| < epsilon
```


Use this function to check whether the result of multiplication of the original matrix and its inverse is approximately equal to the identiy matrix. 

** Note that in the `almost_identity(M, epislon)` function, you must not use any `if` statements (use the `assert` statement). **