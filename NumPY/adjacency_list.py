def adjacency_list_to_matrix(one_param):
    n = len(one_param)
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in one_param[i]:
            matrix[i][j] = 1
    return matrix
adjacency_list_to_matrix()