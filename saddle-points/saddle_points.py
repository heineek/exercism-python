def saddle_points(matrix):
    if not matrix:
        return set()

    maximals_in_rows = []
    for i, row in enumerate(matrix):
        if len(row) != len(matrix[0]):
            raise ValueError
        maximal = row[0]
        for val in row:
            if val > maximal:
                maximal = val
        for j, val in enumerate(row):
            if val == maximal:
                maximals_in_rows.append((i, j, val))

    result = []
    minimals_in_cols= []
    for row, col, val in maximals_in_rows:
        minimal = val
        for i in range(len(matrix)):
            if matrix[i][col] < minimal:
                minimal = matrix[i][col]
        if val == minimal:
            result.append((row, col))

    return set(result)