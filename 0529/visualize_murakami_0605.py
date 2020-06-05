
# coding: utf-8

# In[44]:


import numpy as np
from PIL import Image, ImageDraw
import random


# In[45]:


#データ入力

#生徒数
n = int(input())

#席の数
m1 = int(input())
m2 = int(input())
m = m1*m2

#配置データ
#改行区切り用
# A = [int(input()) for i in range(m1*m2*n)]
#空白区切り用
A = list(map(int, input().split()))

#満足度？
#S = [int(input()) for i in range(n)]


# In[46]:


# #テストデータ

# #生徒数
# n = 30

# #席の数
# m1 = 7
# m2 = 8
# m = m1*m2

# #配置データ
# A = np.zeros(m*n)
# seat = 0
# for i in range(30):
#     A[m*i + seat] = 1
#     seat+=1
#     if(i%4 == 0):
#         seat+=1


# In[47]:


#定数

#席の余白
front = 2
back = 2
lr = 1

#席あたり(1マス)の縦横サイズ
d1 = 160
d2 = 240

#机のサイズ
desk_dy = d1/3
desk_dx = d2/2

#生徒を表す丸の半径
seat_r = d2/6

#使う色
white = (255,255,255)
gray = (128, 128, 128)
black = (0,0,0)
red = (255, 0, 0)
orange = (255, 165, 0)
blue = (0, 0, 205)
sky = (135, 206, 250)
green = (60, 179, 113)
ivory = (248, 244, 230)
wood = (222, 184, 135)


# In[48]:


#席番号から座標を出す関数
def xy(seat):
    return (d2*(seat%m2 + lr), d1*(seat//m2 + front))


# In[49]:


#ベタ画像生成
im = Image.new('RGB', (d2*(m2 + lr*2 - 1), d1*(m1 + front + back - 1)), ivory)
draw = ImageDraw.Draw(im)


# In[50]:


#黒板を置く
w = im.width
draw.rectangle((w/4,d2/4,w*3/4,d2/2), fill = green, outline=black)


# In[51]:


#机を置く

#各マスの上端に置く
for i1 in range(m1):
    for i2 in range(m2):
        y = d1*(i1 + front) - d1/2
        x = d2*(i2 + lr) - desk_dx/2
        draw.rectangle((x, y, x+desk_dx, y+desk_dy), fill=wood, outline=black)
        


# In[52]:


#座らせる

#丸を描く矩形を求める関数
def seat_xy(seat, i):
    #各生徒で丸のサイズ調整したい時はここで変える(現状全員同じ)
    r_i = seat_r
    
    le_up = (d2*(seat%m2 + lr) - r_i, d1*(seat//m2 + front) - r_i) #left_upper
    return (le_up[0], le_up[1], le_up[0] + 2*r_i, le_up[1] + 2*r_i)
    
#各生徒の座席番号
stdnts = np.nonzero(A)[0]
stdnts = stdnts % (m*np.ones(n))

for i in range(n):
    col_i = sky
    
    #試しにランダムに色分けしてみよう
    rand = random.random()
    if(rand < 1/3):
        col_i = red
    elif(rand < 2/3):
        col_i = sky
    else:
        col_i = orange
    
    draw.ellipse(seat_xy(stdnts[i], i), fill=col_i, outline=black)


# In[53]:


#画像出力
im.save('visualize_imagedraw.jpg', quality=95)

