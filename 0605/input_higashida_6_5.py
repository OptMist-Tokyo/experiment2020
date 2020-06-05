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
        students = [] #個人データ(名前と選好項目）
        #1行ずつ全員分の個人データを読み込む
        for i in range(total):
            data = f.readline().split()
            data[1:5] = map(int, data[1:5]) #先頭のname, 末尾のNextTo以外の要素をint型に変換
            students.append(dict(zip(info, data))) #infoをkeyにして個人データを1人分ずつ辞書にまとめる

    summarized = (row, column, total, students)
    return summarized

#summarized_dataにおいて，指定された番号num_of_studentの学生について，そのNextToに対応する学生の番号を返す
#nameの値が重複する学生はいないことを仮定
def find_num(num_of_student):
    i = 0
    nextto = summarized_data[3][num_of_student]['NextTo']
    while i < summarized_data[2]:
        if summarized_data[3][i]['name'] == nextto:
            return i #もし見つかれば番号を返す
        i += 1
    return -1 #見つからなければ-1を返す


#raw_dataを受け取り，データをsummarized_dataにまとめる
raw_data = 'input_sample_full1.txt' #サンプルデータ
summarized_data = summarize(raw_data)

#NextToの値-1もstr型であることに注意
