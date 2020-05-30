'''
入力形式：
1行目：座席の行数，列数
2行目：学生の総数
3行目以降：
各行ごとに
    名前と選好度(ここでは1～5とする)

以下，.txtでの読み込みを想定
'''

#rawのデータをsummarizedにまとめる
def summarize(raw):
    with open(raw) as f:
        row, column = map(int, f.readline().split()) #1行目：座席の行数，列数
        total = int(f.readline()) #2行目：学生の総数

        #3行目以降
        students = [] #個人データ(名前と選好項目）
        info = ('name', 'p_blackboard', 'p_airconditioner', 'p_corner', 'p_interval') #pはpreferenceの頭文字
        #1行ずつ全員分の個人データを読み込む
        for i in range(total):
            data = f.readline().split()
            data[1:] = map(int, data[1:]) #先頭のname以外の要素をint型に変換
            students.append(dict(zip(info, data))) #infoをkeyにして個人データを1人分ずつ辞書にまとめる

    summarized = (row, column, total, students)
    return summarized


#raw_dataを受け取り，データをsummaized_dataにまとめる
raw_data = 'input_sample1.txt' #サンプルデータ
summarized_data = summarize(raw_data)
#print(summarized_data)
