import numpy as np

# создание матрицы из условия
def create_matrix(n, m):
    ret_matrix = []
    temp_matrix = []
    for i in range(n):
        for j in range(n):
            if (i == j):
                temp_matrix.append(n + (m ** 2) + (j + 1) / m + (i + 1) / n)
            else:
                temp_matrix.append(((i + j + 2) / (m + n)))
        temp_matrix.append(30 + 20 * (i + 1))
        ret_matrix.append(temp_matrix)
        temp_matrix = []
    return ret_matrix

# чтение матрицы из файла
def create_matrix_from_file(file_name):
    array = []
    dim = []
    with open(file_name) as input_file:
        for line in input_file:
            line = line.strip()
            for number in line.split():
                array.append(float(number))
        dim.append(int(array[0]))
        dim.append(int(array[1]))
    if (dim[0] + dim[1] != len(array) + 2):
        print("Wrong input file")
        return None
    array = array[2:]
    array = np.array(array)
    array.resize((dim[0], dim[1]))
    array = array.tolist()
    return array

# меняет строки местами
def swap_lines(A, f, row1, row2):
    for i in range(len(A)):
        A[row1][i], A[row2][i] = A[row2][i], A[row1][i]

    try:
        for i in range(len(f)):
            f[row1][i], f[row2][i] = f[row2][i], f[row1][i]
    except:
        f[row1], f[row2] = f[row2], f[row1]

    return A, f

# прибавляет строку, умноженную на число
def add_line_to_line(A, row1, row2, elem):
    if A == []:
        return []
    try:
        for i in range(len(A[row1])):
            A[row1][i] += A[row2][i] * elem
    except TypeError:
        A[row1] += A[row2] * elem
    return A

# метод Гаусса
def gauss(A, f=[]):
    if f == []: f = [0.] * len(A)
    find_j = -1
    epl = 1e-9
    used_row = set()

    # метод Гаусса (с выбором главного элемента):
    max_elem = -1
    for j in range(len(A)):
        for i in range(len(A)):
            if abs(A[j][i]) > epl and j not in used_row and max_elem < abs(A[j][i]):
                max_elem = abs(A[j][i])
                find_j = j
        if find_j == -1:
            break
        A, f = swap_lines(A, f, find_j, i)
        temp = A[find_j][j]

        try:
            for j in range(len(f)):
                f[find_j][j] /= temp
        except:
            f[find_j] /= temp

        for j in range(len(A)):
            A[find_j][j] /= temp

        for j in range(len(A)):
            if j != find_j:
                f = add_line_to_line(f, j, find_j, -A[j][i] / A[find_j][i])
                A = add_line_to_line(A, j, find_j, -A[j][i] / A[find_j][i])
        used_row.add(find_j)
    return f

# норма матрицы
def norm(a):
    res = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            res += a[i][j] ** 2
    return np.sqrt(res)

# число обусловленности
def number(A):
    n = len(A)
    BA = list(np.copy(A))
    CA = np.eye(n)
    BA = gauss(BA, CA)
    CA = norm(BA) * norm(A)
    return CA

# определитель матрицы
def det(A):
    return np.linalg.det(A)
