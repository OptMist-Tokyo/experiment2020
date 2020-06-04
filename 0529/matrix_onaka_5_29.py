import numpy as np


def C(i):  # 椅子の番号を与えると座標を返してくれる関数
    x = i % h - 5
    if x >= 0:
        x += 1
    y = i // h
    return x, y


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
