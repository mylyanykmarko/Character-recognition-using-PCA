from matrix import transpose, multiply, print_matrix


# Finds sample mean of observation vectors, there - each photo of the letter
def sample_mean(matrix):
    N = len(matrix[0])
    M = list()
    for i in range(len(matrix)):
        M.append(int(1 / N * sum(matrix[i])))
    return M


# Transforms matrix into mean deviation form
def to_mean_deviation_form(matrix, mean):
    n = len(matrix)
    m = len(matrix[0])
    B = [[0 for i in range(m)] for j in range(n)]

    for row in range(n):
        for col in range(m):
            B[row][col] = matrix[row][col] - mean[row]

    return B


# Final formula
def cov_matrix(n, B):
    m = multiply(B, transpose(B))
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] *= 1 / (n - 1)
    return m


def find_cov_matrix(matrix):
    mean = sample_mean(matrix)
    b = to_mean_deviation_form(matrix, mean)
    return cov_matrix(len(matrix[0]), b)
