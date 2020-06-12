'''
入力形式：
1行目：座席の行数，列数
2行目：学生の総数
3行目以降：
各行ごとに
    名前と選好度(ここでは1～5とする), 隣に座りたい人（希望があればその人の名前，なければ-1が入る）

以下，.txtでの読み込みを想定
'''

info = ('name', 'Blackboard', 'Window','Airconditioner','Edge','NextTo') #選好に対応する命名

#rawのデータをsummarizedにまとめる
def summarize(raw):
    with open(raw, encoding = 'utf-8') as f:
        row, column = map(int, f.readline().split()) #1行目：座席の行数，列数
        total = int(f.readline()) #2行目：学生の総数

        #3行目以降
        #studentsは key:[選好度] の形の辞書
        students = {key:[] for key in info} #選好項目ごとに値をリストにまとめる
        #1行ずつ全員分の個人データを読み込む
        for i in range(total):
            data = f.readline().split()
            data[1:5] = map(int, data[1:5]) #先頭のname, 末尾のNextTo以外の要素をint型に変換
            j = 0
            for key in info:
                students[key].append(data[j])
                j += 1
        
    summarized = (row, column, total, students)
    return summarized

#raw_dataを受け取り，データをsummarized_dataにまとめる
raw_data = 'input_sample_full1.txt' #サンプルデータ
summarized_data = summarize(raw_data)

#NextToの値-1もstr型であることに注意


#計算用にsummarized_data[3]からリストの値をコピー
u_Blackboard = summarized_data[3]['Blackboard'][:]
u_Window = summarized_data[3]['Window'][:]
u_Airconditioner = summarized_data[3]['Airconditioner'][:]
u_Edge = summarized_data[3]['Edge'][:]
u_NextTo = summarized_data[3]['NextTo'][:]
