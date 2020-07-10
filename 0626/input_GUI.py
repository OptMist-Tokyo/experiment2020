# coding: utf-8

import sys
import tkinter as tk
import tkinter.ttk as ttk

#自然数か否か判定
def is_N(entry):
    if entry.isdecimal() and int(entry) > 0:
        return True
    else:
        return False


#rootウィンドウの内容確認
def check_root(root, val0, val1, val2, warning):
    #型判定
    if is_N(val0) and is_N(val1) and is_N(val2):
        #定員以内か否か判定
        if int(val0) * int(val1) >= int(val2):
            warning['text'] = ''
            global summarized_data_forDemo
            summarized_data_forDemo = [int(val0), int(val1), int(val2)]
            create_detailWindow(root)
        else:
            warning['text'] = '定員オーバーです。'
    else:
        warning['text'] = '1以上の整数を半角で入力してください。'


#rootウィンドウの生成
def create_root(root):
    root.title(u"Seat Arrangement Optimizer")

    label1 = tk.Label(text = '教室の大きさ、及び人数を入力してください。')
    label1.grid(columnspan = 2)

    labe1forRow = tk.Label(root, text = '縦')
    labe1forRow.grid(row=1, column = 0) 
    entryforRow = tk.Entry(root)
    entryforRow.grid(row = 1, column = 1)

    labe1forColumn = tk.Label(root, text = '横')
    labe1forColumn.grid(row=2, column = 0) 
    entryforColumn = tk.Entry(root)
    entryforColumn.grid(row = 2, column = 1)

    labe1forTotal = tk.Label(root, text = '人数')
    labe1forTotal.grid(row=3, column = 0) 
    entryforTotal = tk.Entry(root)
    entryforTotal.grid(row = 3, column = 1)

    warning = tk.Label(root, text = '', fg = '#ff0000')
    warning.grid(row=4, column=0, columnspan=2)

    nextButton = tk.Button(root, text = '次へ', command = lambda:check_root(root, entryforRow.get(), entryforColumn.get(), entryforTotal.get(),  warning))
    nextButton.grid(row=5, column=0, columnspan = 2)


#選好入力用ウィンドウの入力欄作成
def create_widgets(window, i):
    choice = [str(j) for j in range(10+1)]
    widgets = [tk.Label(window, text='{}人目'.format(str(i+1)))]
    widgets.append(tk.Entry(window, width = 15))
    for j in range(lengthofInfo-2):
        widgets.append(ttk.Combobox(window, values = choice, width = 10))
    widgets.append(tk.Entry(window, width=15))
    widgets[lengthofInfo].insert(0, 'なし')
    return widgets


#選好入力用ウィンドウの内容確認
def check_detailWindow(detailWindow, inputs_list, warnings):
    total = summarized_data_forDemo[2]
    choice = [str(j) for j in range(10+1)]
    
    flag0 = True #名前
    flag1 = True #選好の値
    flag2 = True #隣の人
    
    #0列目：名前の確認
    for i in range(total):
        tmp = [inputs_list[i][0] for i in range(summarized_data_forDemo[2])]
        if inputs_list[i][0] == '': #名前欄が空の場合
            warnings[0]['text'] = '全ての欄に名前を入れてください。'
            flag0 = False
        elif tmp.count(inputs_list[i][0]) > 1: #名前が被っている場合
            warnings[0]['text'] = '名前が重複しています。'
            flag0 = False
    if flag0:
        warnings[0]['text'] = ''
    
    #1~4列目：数字で選ぶ選好の確認
    i = 0
    while i < total:
        j = 0
        while j < lengthofInfo - 2:
            if not (inputs_list[i][j+1] in choice): #1~5の整数以外の入力は全て違反
                warnings[1]['text'] = '0~10の整数を半角で入力してください。'
                flag1 = False
                break
            j += 1
        if flag:
            break
        elif sum(inputs_list[i][1:lengthofInfo-1]) != 10: #選好度の合計は10でなければならない
            warnings[1]['text'] = '合計が10になるよう入力してください。'
            flag1 = False
            break
        i += 1
    if flag1:
        warnings[1]['text'] = ''
    
    #5列目：隣に座りたい人の名前の確認
    if flag0: #学生の名前に空欄があると，隣の希望なしの空欄と混同するので，これを防ぐ。
        tmp_name = [inputs_list[i][0] for i in range(total)]
        for i in range(total):
            k = inputs_list[i][lengthofInfo-1]
            if k == inputs_list[i][0]: #自分自身の名前を入力している場合
                warnings[2]['text'] = '自分以外の名前を入力してください。\n希望がない場合は「なし」と入力してください。'
                flag2 = False 
            elif k != 'なし' and not (k in tmp_name): #リクエストと同じ名前の人がいないとき
                warnings[2]['text'] = 'リクエストと同じ名前の人が見つかりません。\n希望がない場合は「なし」と入力してください。'
                flag2 = False 
        if flag2:
            warnings[2]['text'] = ''

        if flag0 and flag1 and flag2:
            create_checkWindow(detailWindow, inputs_list)


#選好入力用のウィンドウの生成
def create_detailWindow(root):
    detailWindow = tk.Toplevel(root)
    total = summarized_data_forDemo[2]

    #学生数が大きい場合に備えてスクロールバーが必要
    #だが実装が間に合わず……

    #0行目：指示
    txt = '名前と希望の度合いを入力してください。'
    instruction = tk.Label(detailWindow, text = txt)
    instruction.grid(column = 3, columnspan = 2)

    #1行目：警告文
    warning_Name = tk.Label(detailWindow, text = '', fg = '#ff0000')
    warning_Name.grid(row = 1, column = 0, columnspan = 2)
    warning_Value = tk.Label(detailWindow, text = '', fg = '#ff0000')
    warning_Value.grid(row = 1, column = 3, columnspan = 2)
    warning_NextTo = tk.Label(detailWindow, text = '', fg = '#ff0000')
    warning_NextTo.grid(row = 1, column = lengthofInfo)
    warnings = (warning_Name, warning_Value, warning_NextTo)

    #2行目：項目
    space = tk.Label(detailWindow, text='')
    space.grid()
    for i in range(lengthofInfo):
        label = tk.Label(detailWindow, text=info_j[i])
        label.grid(row = 2, column = i+1)

    widgets_list = [create_widgets(detailWindow, i) for i in range(total)]

    #3~(total+2)行目：入力欄
    for i in range(total):
        for j in range(lengthofInfo+1):
            if j != lengthofInfo:
                widgets_list[i][j].grid(row = i+3, column = j)
            else:
                widgets_list[i][j].grid(row = i+3, column = j, columnspan = 2)

    #(total+3)行目：空白
    space = tk.Label(detailWindow, text='')
    space.grid(row = total + 3)

    #(total+4)行目：確認ボタン
    check_button = tk.Button(detailWindow, text = '確認', command= lambda:check_detailWindow(detailWindow, [[widgets_list[i][j+1].get() for j in range(lengthofInfo)] for i in range(total)], warnings))
    check_button.grid(row = total + 4, column = 2, columnspan = 3)


#確認画面のウィジェット生成
def create_widgetsforCheck(window, inputs_list, i):
    widgets = [tk.Label(window, text='{}人目'.format(str(i+1)))]
    for j in range(lengthofInfo):
        widgets.append(tk.Label(window, text = inputs_list[i][j]))
    return widgets


#確認画面の生成
def create_checkWindow(detailWindow, inputs_list):
    checkWindow = tk.Toplevel(detailWindow)
    total = summarized_data_forDemo[2]

    #学生数が大きい場合に備えてスクロールバーが必要

    #0行目：指示
    instruction = tk.Label(checkWindow, text = '確認')
    instruction.grid(row = 0, column = 3, columnspan = 2)

    #1行目；入力内容の確認表示（教室サイズ）
    label1 = tk.Label(checkWindow, text = '縦：'+ str(summarized_data_forDemo[0]))
    label1.grid(row = 1, column = 3)
    label2 = tk.Label(checkWindow, text = '横：'+ str(summarized_data_forDemo[1]))
    label2.grid(row = 1, column = 4)

    #2行目：選好名
    for i in range(lengthofInfo):
        label = tk.Label(checkWindow, text=info_j[i])
        label.grid(row = 2, column = i+1)

    widgets_list = [create_widgetsforCheck(checkWindow, inputs_list, i) for i in range(total)]

    #3~(total+2)行目：入力内容の確認表示（各学生の選好項目）
    for i in range(total):
        for j in range(lengthofInfo+1):
            widgets_list[i][j].grid(row = i+3, column = j)

    #(total+3)行目：修正ボタン
    modify_button = tk.Button(checkWindow, text = '修正する', command = checkWindow.destroy) #修正する場合は確認画面を閉じ，詳細入力画面に戻る
    modify_button.grid(row = total + 3, column = 2, columnspan = 3)
    #(total+4)行目：決定ボタン
    check_button = tk.Button(checkWindow, text = '決定する', command = lambda:summarize(inputs_list)) #確定する場合は，詳細データを格納
    check_button.grid(row = total + 4, column = 2, columnspan = 3)


#結果を summarized_data_forDemo にまとめる
def summarize(inputs_list):
    global summarized_data_forDemo
    students = {key:[] for key in info} #選好項目ごとに値をリストにまとめる
        #1行ずつ全員分の個人データを読み込む
    for i in range(summarized_data_forDemo[2]):
        data = inputs_list[i]
        data[1:5] = map(int, data[1:5]) #先頭のname, 末尾のNextTo以外の要素をint型に変換
        j = 0
        for key in info:
            if key != 'NextTo':    
                students[key].append(data[j])
                j+= 1
            else:
                if data[j] == 'なし':
                    students[key].append(str(-1))
                else:
                    students[key].append(data[j])
    summarized_data_forDemo.append(students)
    root.quit()



#選好名
info = ('name', 'Blackboard', 'Window','Airconditioner','Edge','NextTo') 
info_j = ('名前', '黒板の近くの席がいい', '窓のそばの席がいい', 'エアコンから離れた席がいい', '端の席がいい', '知り合いの隣がいい')
lengthofInfo = len(info)

#入力を格納するリスト。前のコードだと summarized_data に相当。
#これはデモ用として，実際の計算の際には前と同様に.txtのデータを使って summarized_data にまとめる方がいいかも（入力が大変なので）。
summarized_data_forDemo = []

#GUIの作成
root = tk.Tk()
create_root(root)
root.mainloop()

#結果の確認
#print(summarized_data_forDemo)
