#cosing: utf-8
#Dummy Japanese character: あ
#Gurobi Optimizerのパッケージをインポート

import gurobipy as gp
import pandas as pd

# 学生番号の集合を定義：学生N人
N = 30 #てきとう
I = [i for i in range(N)]

# 席位置の集合を定義：縦K行、横L列
K = 7 #てきとう
L = 10
J = [j for j in range(K*L)]
# 前方左側を0，そこから右に1,2,...と番号を振る．
# j\in Jは前からj//L番目，左からj%p番目の席を表す．


#効用関数とそれぞれの選好を定義
u_Blackboard = {}
u_func_BB = {}
u_Window = {}
u_Airconditioner = {}
u_Edge = {}

#それぞれの席における距離や、属性を定義
distance_from_blackboard = {}
Window = {}
Airconditioner = {}
Edge = {}

for i in range(K):
    for j in range(L):
        distance_from_blackboard[i*L + j] = i + 1

for i in range(K):
    for j in range(L):
        if j==0:
            Window[i*L + j] = 1
        else:
            Window[i*L + j] = 0

for i in range(K):
    for j in range(L):
        if j==7:
            Airconditioner[i*L + j] = 1
        else:
            Airconditioner[i*L + j] = 0

for i in range(K):
    for j in range(L):
        if j==0　or j==4 or j==5 or j==9:
            Edge[i*L + j] = 1
        else:
            Edge[i*L + j] = 0


#目的関数の係数となるCを定義
c_Blackboard = {}
c_Window = {}
c_Airconditioner = {}
c_Edge = {}



for i in range I:
    for j in range J:
        c_Blackboard[i,j] = u_Blackboard[i] * u_func_BB[j]

for i in range I:
    for j in range J:
        c_Window[i,j] = u_Window[i] * Window[j]

for i in range I:
    for j in range J:
        c_Airconditioner[i,j] = u_Airconditioner[i] * Airconditioner[j]

for i in range I:
    for j in range J:
        c_Edge[i,j] = u_Edge[i] * Edge[j]
