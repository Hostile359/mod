import cmath
import math

import matplotlib.pyplot as plt
import random
from collections import Counter
from scipy.stats import binom


def lab0():
    values_dict = {}
    
    for i in range(1001):
        values_dict[float(i / 1000)] = 0
    
    for _ in range(10**7):
        val = random.random().__round__(3)
        values_dict[val] += 1
    
    with open('data1.csv', 'w') as file:
        for key, val in values_dict.items():
            line = f'{key};{val}\n'
            file.write(line)
    # x_list = [random.random().__round__(3) for _ in range(10**7)]
    # # print(Counter(x_list))
    # plt.hist(x_list)
    # # plt.yticks([10**5, 10**6])
    # plt.savefig('plt.png')


func1 = 0.3


def func2(x):
    return 0.9 * (x - 2) ** 2


def func_1(x):
    return x


def func_2(x):
    return 2 - 1.05409 * math.sqrt(x)


def lab1():
    x_list = []
    y_list = []

    for _ in range(10**6):
        x = random.uniform(0, 2)
        if x < 1:
            y = func1
        else:
            y = func2(x)

        x_list.append(x)
        y_list.append(y)

    plt.scatter(x_list, y_list, marker='.')
    plt.savefig('lab1.png')
    plt.show()


def lab11():
    y_list = []
    for _ in range(10**6):
        x = random.uniform(0, 1)
        y = func_1(x)
        y_list.append(y)
    for _ in range(10**6):
        x = random.uniform(0, 0.9)
        y = func_2(x)
        y_list.append(y)
    plt.hist(y_list)
    # plt.savefig('lab11.png')
    plt.show()


def C_k_n(k, n):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def C__k_n(k, n):
    return math.factorial(k + n - 1) / (math.factorial(n - 1) * math.factorial(k))


def p_balls_noback(k, n, K, N):
    _1 = C_k_n(k=k, n=K)
    _2 = C_k_n(k=n-k, n=N-K)
    _3 = C_k_n(k=n, n=N)
    # print(_1, _2, _3)
    return (_1 * _2) / _3


def p_balls_back(k, n, K, N):
    _1 = C__k_n(k=k, n=K)
    _2 = C__k_n(k=n-k, n=N-K)
    _3 = C__k_n(k=n, n=N)
    # print(_1, _2, _3)
    return (_1 * _2) / _3


def lab12(dist_fun, pic_filename):
    x_list = []
    for k in range(6):
        x_list.append(dist_fun(k=k, n=5, N=18, K=10))
        print(x_list[-1])
    print(sum(x_list))

    p_list = []
    summa = 0
    for x in x_list:
        summa += x
        p_list.append(summa)
    print(p_list)

    x_list = []
    y_list = []
    for _ in range(10**6):
        x = random.uniform(0, 1)
        for p_i in p_list:
            if x < p_i:
                x_list.append(x)
                y_list.append(p_i)
                break

    # plt.hist(y_list)
    plt.scatter(x_list, y_list)
    plt.savefig(pic_filename)
    plt.show()
    # exit(0)
    #
    #
    # y_list = []
    # for k in range(6):
    #     y_list.append(p_balls_back(k=k, n=5, N=18, K=10))
    #     print(y_list[-1])
    # print(sum(y_list))
    # plt.hist(y_list)
    # plt.savefig('lab13.png')
    # N = 10
    # p = 0.8
    # x_list = []
    # k_list = [k for k in range(N)]
    # for k in k_list:
    #     x_list.append(binom.pmf(k=k, n=N, p=p))
    # print(sum(x_list))
    # p_list = []
    # summa = 0
    # for x in x_list:
    #     summa += x
    #     p_list.append(summa)
    # print(p_list)
    # y_list = []
    # for _ in range(10**6):
    #     x = random.uniform(0, 1)
    #     for p_i in p_list:
    #         if x < p_i:
    #             y_list.append(p_i)
    #             break
    # plt.hist(y_list)
    # plt.show()


# lab1()
# lab11()
lab12(dist_fun=p_balls_noback, pic_filename='lab12.png')
lab12(dist_fun=p_balls_back, pic_filename='lab13.png')
