# Prints list of lists in form of matrix
def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    print("_" * 2 * m)
    for row in range(n):
        print("|" + "|".join([str(num) for num in matrix[row]]) + "|")
    print("_" * 2 * m)


# Transposes matrix
def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[0 for col in range(n)] for row in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed


# Multiplies two vectors
def inner_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


# Multiply two matrices
def multiply(matrix1, matrix2):
    product = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
    for row in range(len(matrix1)):
        for col in range(len(matrix2[0])):
            product[row][col] = inner_product(matrix1[row], [row1[col] for row1 in matrix2])

    return product
