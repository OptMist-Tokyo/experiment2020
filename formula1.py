# coding: utf-8
# Dummy Japanese character: あ（意味はないが確実に日本語を含むファイルにする）
# 参考)https://qiita.com/keisukesato-ac/items/526543004141a1018a51

# Gurobi Optimizerのパッケージをインポートし、
# "gp"という短縮名を設定（違う短縮名にしてもよい）
import gurobipy as gp

# Excelファイルを読み込むためにpandasをインポート(するなら)
# import pandas as pd

# 学生番号の集合を定義：学生N人
N = 30 #てきとう
I = [i for i in range(N)]

# 席位置の集合を定義：縦K行、横L列
K = 7 #てきとう
L = 8
J = [j for j in range(K*L)]
# 前方左側を0，そこから右に1,2,...と番号を振る．
# j\in Jは前からj//L番目，左からj%p番目の席を表す．

## 選好の定義
# 各個人の位置だけで定まる選好 c_1,c_2,...
# 総計 c[i,j] = sum(c_k[i,j])

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
model.setObjective(gp.quicksum(c[i,j]*x[i,j] for i in I for j in J)
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
print("[Gurobi Optimizerログ]")

model.optimize()

print()

# 最適解が得られた場合、結果を出力
print("[解]")
if model.Status == gp.GRB.OPTIMAL:
   print("    最適解: ")
   for i in I:
       for j in J:
           if x[i, j].X > 0.98:
               print(f"        学生{i}は前から{j//L}番目,左から{j%L}番目に座る")
# 最適値の表示．この場合の最適値に費用のような意味はないので省いてよさそう
# val_opt = model.ObjVal
# print(f"    最適値: {val_opt}")
