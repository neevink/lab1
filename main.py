# Neevin Kirill
# variant number: 12
# Метод Гаусса-Зейделя

import itertools
import sys
from copy import deepcopy
from typing import List


def norm(matrix: List[List]) -> float:  # Находит норму матрицы и определяет сходится ли
    return max([sum(map(lambda x: abs(x), row)) for row in matrix]) <= 1


def print_matrix(matrix: List[List]) -> None:
    for e in matrix:
        print(e)
    print()


def solve(coefficients: List[List], ans: list, epsilo: float = 0.01, max_iter_count: float = 100):
    n, k, q = len(coefficients), 0, epsilo
    roots = deepcopy(ans)

    while k < max_iter_count and q >= epsilo:
        k += 1
        q = 0
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += coefficients[i][j] * roots[j]

            xi = (ans[i] - s) / coefficients[i][i]
            diff = abs(xi - roots[i])
            if diff > q:
                q = diff
            roots[i] = xi

    if k > max_iter_count:
        print('Итерация расходится')
    else:
        return [round(e, 2) for e in roots]


def check(matrix: List[List]) -> bool:  # Проверить выполнилось ли условие преобладания диагональных элементов
    n = len(matrix)
    for i in range(n):  # строка
        ok = True
        for j in range(n):  # столбец
            if abs(matrix[i][i]) < abs(matrix[i][j]):
                ok = False
                break
        if not ok:
            return False
    return True


def reorder_matrix():  # Переставить строки матрицы так, чтобы выполнялось условие пробл. диаг. эл-ов
    for perm in itertools.permutations(m):
        if check(perm):
            return list(perm)
    return None


def input_matrix():
    epsilon = float(input('Введите погрешность: '))
    n = int(input('Введите количество уравнений: '))
    print('Введите коэф. ур-я при x и свободные члены: x_11 x_12 ... = b1')
    coeffs = [list(map(float, input(f'Строка {z+1}: ').split())) for z in range(n)]

    return epsilon, n, coeffs


def read_file():
    path = input('Введите путь к файлу: ')
    with open(path, 'r') as f:
        epsilon = float(f.readline())
        n = int(f.readline())
        matrix = []
        for i in range(n):
            matrix.append(list(map(float, f.readline().split())))
        return epsilon, n, matrix


if __name__ == '__main__':
    read_from = input('Прочитать матрицу из файла (f) или с клавиатуры (k)?: ')
    if read_from == 'f':
        e, n , m = read_file()
    else:
        e, n, m = input_matrix()

    print('Исходная матрица: ')
    print_matrix(m)

    m = reorder_matrix()
    if m is None:
        print('Не удалось преобразовать матрицу так, чтобы получить преобл. диаг. эл-ов')
        sys.exit()

    print('Перестановкой строк, получилась матрица:')
    print_matrix(m)

    mm = deepcopy(m)
    # Тут систему преобразуем в матрицу
    for i in range(len(m)):
        a = m[i][i]
        mm[i] = [-m[i][j]/a if i != j else 0 for j in range(len(m[i]))]

    print('C:')
    c = [e[:-1] for e in mm]
    print_matrix(c)

    print('d:')
    d = [e[-1] for e in mm]
    print_matrix(d)

    if not norm(c):
        print('Условие сходимости не выполнено. Решить нельзя.')
        sys.exit()

    for i in range(len(m)):
        a = m[i][i]
        m[i] = [-m[i][j]/a for j in range(len(m[i]))]

    print('Вектор решений равен:')
    print(solve([e[:-1] for e in m], d))
