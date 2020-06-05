# coding: utf-8
# Dummy Japanese character: あ（意味はないが確実に日本語を含むファイルにする）
# 参考)https://qiita.com/keisukesato-ac/items/526543004141a1018a51

# Gurobi Optimizerのパッケージをインポートし、
# "gp"という短縮名を設定（違う短縮名にしてもよい）
import gurobipy as gp

# Excelファイルを読み込むためにpandasをインポート(するなら)
# import pandas as pd

## データ入力
'''
入力形式：
1行目：座席の行数，列数
2行目：学生の総数
3行目以降：
各行ごとに
    名前と選好度(ここでは1～5とする)
以下，.txtでの読み込みを想定
'''
info = ('name','u_Blackboard','u_func_BB','u_Window','u_Airconditioner','u_Edge') #選好に対応する命名
#黒板に関しては片方だけ残しておけばよさそう
#人との距離によって決まるinfoがまだ入っていない
#info = ('name', 'p_blackboard', 'p_airconditioner', 'p_corner', 'p_interval') #元の定義：pはpreferenceの頭文字

def summarize(raw):
    with open(raw) as f:
        row, column = map(int, f.readline().split()) #1行目：座席の行数，列数
        total = int(f.readline()) #2行目：学生の総数
        #3行目以降
        students = [] #個人データ(名前と選好項目）
        #1行ずつ全員分の個人データを読み込む
        for i in range(total):
            data = f.readline().split()
            data[1:] = map(int, data[1:]) #先頭のname以外の要素をint型に変換
            students.append(dict(zip(info, data))) #infoをkeyにして個人データを1人分ずつ辞書にまとめる

    summarized = (row, column, total, students)
    return summarized

raw_data = 'input_data.txt' #txtファイルを入力
summarized_data = summarize(raw_data)


# 学生番号の集合を定義：学生N人
N = summarized_data[2] #total
I = [i for i in range(N)]


# 席位置の集合を定義：縦K行、横L列
K = summarized_data[0] #row
L = summarized_data[1] #column
M = K*L #席数
J = [j for j in range(M)]
# 前方左側を0，そこから右に1,2,...と番号を振る．
# j\in Jは前からj//L番目，左からj%p番目の席を表す．


## 選好の定義

# 席同士の距離と隣接関係の定義
def C(i):  # 椅子の番号を与えると座標を返してくれる関数
    x = i % K - 5
    if x >= 0:
        x += 1
    y = i // K
    return x, y

D = np.zeros((M,M))  # 椅子同士の距離を入れる行列
for i in range(M):
    for j in range(M):
        D[i][j] = np.sqrt((C(i)[0]-C(j)[0])**2+(C(i)[1]-C(j)[1])**2)

B = np.zeros((M,M))  # 椅子同士の隣接関係を入れる行列
for i in range(M-1):
    if (i * 2) % K != 4:
        B[i][i+1] = 1
        B[i+1][i] = 1
    # 前後ろも隣接していると考えたいなら以下の項を入れる
    # if i + K < m
        # B[i][i+K] = 1
        # B[i+K][i] = 1

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

#効用関数とそれぞれの選好を定義
u_Blackboard = [summarized_data[3][i][info[1]] for i in range(N)]
u_func_BB = [summarized_data[3][i][info[2]] for i in range(N)]
u_Window = [summarized_data[3][i][info[3]] for i in range(N)]
u_Airconditioner = [summarized_data[3][i][info[4]] for i in range(N)]
u_Edge = [summarized_data[3][i][info[5]] for i in range(N)]

#目的関数の係数となるCを定義
c_Blackboard = {}
c_Window = {}
c_Airconditioner = {}
c_Edge = {}

for i in range(N):
    for j in range(M):
        c_Blackboard[i,j] = u_Blackboard[i] * u_func_BB[j]

for i in range(N):
    for j in range(M):
        c_Window[i,j] = u_Window[i] * Window[j]

for i in range(N):
    for j in range(M):
        c_Airconditioner[i,j] = u_Airconditioner[i] * Airconditioner[j]

for i in range(N):
    for j in range(M):
        c_Edge[i,j] = u_Edge[i] * Edge[j]

# 各個人の位置だけで定まる選好 c_1,c_2,...
c = {}
for i in range(N):
    for j in range(M):
        c[i,j] = c_Blackboard[i,j] + c_Window[i,j] + c_Airconditioner[i,j] + c_Edge[i,j]

# 他者との距離に応じて定まる選好 d_1,d_2,...
# 総計 d[i,p,j,q] = sum(d_k[i,p,j,q])
# ただし d[i,i,j,q] = 0


## 問題を設定
model = gp.Model(name = "SekiHaichi")

## 変数を設定（変数単体にかかる制約を含む）
# x[学生番号,席位置] を gp.Var クラスのオブジェクト を
# 表す辞書として定義
x = {}
for i in I:
   for j in J:
       x[i,j] = model.addVar(vtype = gp.GRB.BINARY, name = f"x({i},{j})")

## 目的関数を設定
model.setObjective(
   gp.quicksum(c[i,j]*x[i,j] for i in I for j in J)
   +gp.quicksum(d[i,p,j,q]*x[i,p]*x[j,q] for i in I for p in I for j in J for q in J),
   sense = gp.GRB.MINIMIZE)


## 制約を設定
# 各学生が一つの席につく
con_1 = {}
for i in I:
   con_1[i] = model.addConstr(gp.quicksum(x[i,j] for j in J) = 1, name = f"con_1({i})")

# 各席に高々一人の学生が座る
con_2 = {}
for j in J:
   con_2[j] = model.addConstr(gp.quicksum(x[i,j] for i in I) <= 1,
                                name = f"con_2({j})")

# 解を求める計算
# print("[Gurobi Optimizerログ]")
model.optimize()

# 最適解が得られた場合、結果を可視化
if model.Status == gp.GRB.OPTIMAL:
   print("    最適解: ")
   for i in range(N):
       for j in range(M):
           if x[i, j].X > 0.98:
               # 学生iが前から{j//L}番目,左から{j%L}番目に座るという情報を保存
# 可視化した画像を出力

# 最適値の表示．この場合の最適値に費用のような意味はないので省いてよさそう
# val_opt = model.ObjVal
# print(f"    最適値: {val_opt}")
