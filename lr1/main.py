# -*- coding: utf-8 -*-

import sys
import math

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_coefficient(index, prompt):
    try:
        coefficient = sys.argv[index]
    except:
        print(prompt)
        coefficient = input()
    while not is_float(coefficient):
        print(prompt)
        coefficient = input()
    coef = float(coefficient)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if a == 0:
        if b != 0:
            buf = -c / b
            if buf >= 0:
                root = math.sqrt(buf)
                if root == -0 or root == 0:
                    result.append(0)
                elif root > 0:
                    result.append(math.sqrt(root))
                    result.append(-math.sqrt(root))
    elif D == 0.0:
        root = -b / (2.0 * a)
        if root == -0 or root == 0:
            result.append(0)
        elif root > 0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 == -0 or root1 == 0:
            result.append(0)
        elif root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        if root2 == -0 or root2 == 0:
            result.append(0)
        elif root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
    return result


a = read_coefficient(1, 'А:')
b = read_coefficient(2, 'B:')
c = read_coefficient(3, 'C:')
roots = get_roots(a, b, c)
len_roots = len(roots)
if len_roots == 0:
    print('Нет корней')
elif len_roots == 1:
    print('Один корень: {}'.format(roots[0]))
elif len_roots == 2:
    print('Два корня: {} и {}'.format(roots[0], roots[1]))
elif len_roots == 3:
    print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
else:
    print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
