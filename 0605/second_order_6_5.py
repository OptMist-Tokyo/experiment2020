import numpy as np
from numpy.core.multiarray import ndarray


def C(i):  # 椅子の番号を与えると座標を返してくれる関数
    x = i % h - 5
    if x >= 0:
        x += 1
    y = i // h
    return x, y


def mtov(i, j):
    return j*m + i


def vtom(x):
    return (x%m, x/m)


def func_distance(x):  # 距離に対する目的関数
    return -1/(x+1)


def func_relation(x):  # 仲の良い人との距離に対する目的関数
    return 1/(x+1)


h = 10  # 椅子横
v = 10  # 椅子縦

m = h * v  # 席数
n = 100  # 生徒数

D = np.zeros((m, m))  # 椅子同士の距離を入れる行列

for i in range(m):
    for j in range(m):
        D[i][j] = np.sqrt((C(i)[0]-C(j)[0])**2+(C(i)[1]-C(j)[1])**2)

B = np.zeros((m, m))  # 椅子同士の隣接関係を入れる行列

for i in range(m-1):
    if (i * 2) % h != 4:
        B[i][i+1] = 1
        B[i+1][i] = 1
    # 前後ろも隣接していると考えたいなら以下の項を入れる
    # if i + h < m
        # B[i][i+h] = 1
        # B[i+h][i] = 1

U_distance = [summarized_data[3][i][info[6]] for i in range(N)]  # 各人の距離に対する選好

U_relation = np.zeros((n, n))  # 各人同士の仲の良さを入れる行列
Q = np.zeros((m*n, m*n))  # 目的関数の二次の項の行列、最終的にソルバに入れるもの

for i in range(m):
    for j in range(n):
        for i2 in range(m):
            for j2 in range(n):
                Q[mtov(i, j), mtov(i2, j2)] = (U_distance[j]+U_distance[j2]) * func_distance(D[i][i2]) + U_relation[j, j2]*func_relation(D[i][i2])