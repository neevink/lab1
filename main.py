import itertools
import sys
from copy import deepcopy
from typing import List

# Neevin Kirill
# variant number: 12
# Метод Гаусса-Зейделя


def determinant(m: List[List]) -> float:
    ans = 0
    for x in range(len(m)): # передвигаемся по оси x
        mul_pl, mul_mn = 1, 1
        for j in range(len(m)): # перемножаем элементы по диагонали
            mul_pl *= m[j][j-x]
            mul_mn *= m[j-x][-j]
        ans += mul_pl - mul_mn
    return ans


def norm(m: List[List]) -> float:  # Находит норму матрицы и определяет сходится ли
    return max([
        sum(map(lambda x: abs(x), row)) for row in m
    ]) <= 1


def print_matrix(m: List[List]) -> None:
    for e in m:
        print(e)
    print()


def input_matrix():
    e = int(input('Введите погрешность: '))
    n = int(input('Введите количество уравнений: '))
    print('Введите коэффициенты уравнения при x и свободные члены: ')
    m = [list(map(int, input(f'Строка {i+1}: ').split())) for i in range(n)]

    print_matrix(m)


def solve(coefficients: List[List], ans: list, epsilo: float, max_iter_count: float):
    # a - коэффициенты системы
    # e - погрешность
    # m - максимальное количество итераций

    n = len(coefficients)
    roots = deepcopy(ans)  # берём последний столбец матрицы

    k = 0
    q = epsilo
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
        print(k, diff, roots)
    if k > max_iter_count:
        print('Итерация расходится')
    else:
        return roots


def check(m) -> bool:  # Проверить выполнилось ли условие преобладания диагональных элементов
    n = len(m)
    for i in range(n):  # строка
        ok = True
        for j in range(n):  # столбец
            if abs(m[i][i]) < abs(m[i][j]):
                ok = False
                break
        if not ok:
            return False
    return True


def reorder_matrix():  # Переставить элементы матрицы так, чтобы выполнялось условие пробл. диаг. эл-ов
    for perm in itertools.permutations(m):
        if check(perm):
            return list(perm)
    return None


if __name__ == '__main__':
    # input_matrix()
    m = [
        [2, 2, 10, 14],
        [10, 1, 1, 12],
        [2, 10, 1, 13],
    ]

    # m = [
    #     [16, 12, 300],
    #     [-3, 6, 90],
    # ]

    # m = [
    #     [2, 3, 4, -8],
    #     [1, 3, 6, 0],
    #     [5, 7, 2, -27]
    # ]

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

    print('Вот:')
    print([e[:-1] for e in m])
    print([e[-1] for e in m])
    print(solve([e[:-1] for e in m], d, 0.01, 100))
