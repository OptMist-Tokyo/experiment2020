# 5月8日
- https://docs.google.com/document/d/1eD-4JQwBQO9U3t5-7zl-iwrHriJWkTZRyCujCzrAXaY/edit
とりあえず「6号館教室の座席配置を最適化」することに決定
定式化をしたいので、来週までにそれを考えてくる

# 5月18日
- https://drive.google.com/open?id=18MmEX1dCM42hhlbn_X7frJMOKpIokjI_ (by大中)
-- https://drive.google.com/file/d/18MmEX1dCM42hhlbn_X7frJMOKpIokjI_/view(修正後リンク)
- http://usi3.com/optimal-seat-allocation-at-banquet.html (by東田)
ここまではどちらも二次計画として定式化している。様々な効用を考えている。
- https://www.ipsj-kyushu.jp/page/ronbun/hinokuni/1007/C2/C2-3.pdf (by佐藤)
グラフを用いて定式化した例

# 5月22日
- 二次計画問題として定式化したが、"前に人がいない"という条件を考えようとすると行列の対称性が崩れて面倒
- 立ち見をどのように処理するか
  - 立ち見のスペースを先に確保しておいて、0-1変数で管理する
- 貪欲なアルゴリズム（?）と最適解を比較しても楽しそう→計算量は大丈夫？
- 距離に反比例する効用と、比例する効用をどうバランスよく加味するか
- https://docs.google.com/document/d/1QpkhLUOC5uwh314LF24qTn6gN6xwJDB1UmntduA_CNU/edit (定式化 by東田)
- 順番に座っていくのを考えると、逐次最適化の方が向いているかも…? (by川合)
- 項目ごとでなくて、何を一番優先するかの情報が大切そう(by東田)
- 仲良い人と隣になる→制約条件として定式化できそう
  - https://drive.google.com/file/d/1p6NLHphOT0vy0hiE4TTaqnxMUj5hR3EG/view (by大中)
- 定式化について色々まとめてみた(by 佐藤)
  - https://docs.google.com/document/d/1HS_pr-34JD3IUTi1D-M_yShCIn3wknpK2a3tEDoP_iE/edit
  - 参考: https://www.slideshare.net/MikioKubo/gurobi-python
  
- 他の生徒と離れている→隣接していない、だけで実装できるのはなかろうか

- 役割分担終了
- https://github.com/OptMist-Tokyo/experiment2020/blob/master/formula1.py (by川合)

- 立ち見をどのように処理するか

# 5月29日
やるべきことリスト  
├─二次形式での最適化(今定式化してるやつ)  
│　└─標準入力で決められたフォーマットの.txt(.csv?)を渡しコードを実行すると席順(.txt?)が返ってくるようにする  
│　　　├─各人がnumpyだのpandasだのlistだのでかなりバラバラにコードを作ってるので、一番便利そうな形式に統一  
│　　　├─global変数(=const)とか変数の名前とかを統一  
│　　　├─距離に対する効用関数をどう設定するか  
│　　　└─効用ごとの重み付けをどうするか  
│　  
│　└─標準入力をどうするか  
│　　　├─まずは.txt(.csv?)形式で用意してあげる  
│　　　└─時間があれば、ビジュアライズできるといい(サーバに置かないまでもローカルで動くようなものを作る)  
│　　　　　└─cssとか使ってできそう？？ここら辺全くわかんないです  
│　  
│　└─出力をどう図示するか  
│　　　├─席は6号館ぽくしたいので、左右5個ずつは繋げたい  
│　　　├─人に番号なりの識別できる要素が欲しい  
│　　　└─色分けは効用の高さを反映しても良さそう  
│　　　　　└─色によってどんなタイプの人か表して、効用が高いほど塗りつぶしも濃くするみたいな  
│　  
│　└─Gurobiの使い方  
│　　　└─調べる！各自インストールできるならしといたほうが捗りそう  
│　  
├─webサービスっぽく  
│　├─サーバ使うの面倒らしいので、やらないかも  
│　└─時間がある、もしくはこういう経験をしてみたいって人がいたらやりましょう  
│　  
└─他の定式化  
　　├─局所最適化  
　　│　└─焼きなまし法(SA法)、遺伝的アルゴリズム(GA)、乱択法  
　　└─目的関数は?  
　　　　└─全体効用最大化 or minmax(不幸な人の不幸度を小さくする) or 安定(どの2人を入れ替えても効用が上がらない)→逐次入れ替えて規定ループ数を超えたら(or効用が上がらなくなったら)停止  

# 6月5日
- gurobiはめんどくさそうなので一旦pulpで頑張る(or Matlab)
- https://colab.research.google.com/drive/1853kZ5_mNCC0okbCxjpD6TxDiXpwCeaK?usp=sharing (google colabのファイル)
- 来週は二次以上と可視化、入力の標準化を頑張る

# 6月7日
- 発表用スライドの仮案を作ったので、次回から実験中に暇な人はスライドに書く内容を考えていきましょう！
-- https://drive.google.com/file/d/1TbGzVl-TYmn8V9VlzbOkfVkMCPleblbA/view?usp=sharing (by佐藤) 
-- O'Reilly本のパロディです

- みんなで編集するときは https://drive.google.com/file/d/1TbGzVl-TYmn8V9VlzbOkfVkMCPleblbA/view?usp=sharing を使う

# 6月12日
- 二次計画の部分を組み込んだ
- 組み込むことには成功し、実行も出来たが…
- PuLPには二次計画ソルバーが入っていない！！
- CVXOPTを使うことに→整数制約が組み込めない!!
- CVXPYを使うことに→整数計画は実行できるが…→そもそも凸計画ではなかった！！！
- matlabを使って非凸計画問題を解くのか、Gurobiを使うのか、それとも…→頑張って凸っぽくできればいいのでは？
- 単位行列を二次係数行列Qに足したり引いたりしても、目的関数値は定数しか変わらない→これによって正定値にしたりできる！
- なんかわからんけど、とにかくエラーは消えた
- 二次計画まで統合して目的関数を完成させる(https://colab.research.google.com/drive/1853kZ5_mNCC0okbCxjpD6TxDiXpwCeaK?usp=sharing で編集できます)
- 結果の画像が正しく出るようデバッグ
- インプットのやり方を考える(txtファイルでもいいけど、GUIのボタンとかで簡単に入力できると良さそう)(イメージとしては  https://qiita.com/nnahito/items/ad1428a30738b3d93762)
- スライド作成→体裁は置いといて、とりあえず書く内容を決める(https://drive.google.com/file/d/1TbGzVl-TYmn8V9VlzbOkfVkMCPleblbA/view?usp=sharing で編集できます)

https://jp.mathworks.com/help/optim/ug/quadprog.html
https://jp.mathworks.com/help/optim/examples/mixed-integer-quadratic-programming-portfolio-optimization.html

- https://drive.google.com/file/d/1NVqSoPD67hcpvCG6Mv4FVpW_fgdqgIVz/view (by大中)

# 6月19日
- booleanをTrueにするととんでもなく時間がかかるので、今回はinteger制約にして、かつ非負制約にすることで改善(?)

- 二次計画でなく定式化できないかと考えていた。局所探索の局所最適解から抜け出す方法→アニーリングや、入れ替え方のアイディア(大中)
- 名前を入れた。矢印は片方向。大きさ調整→こちらの想定している出力をまずは私ておく
- スライドやっていた。入力について、まずは規格を決めておきたい。なる早→
- スライドと、普通のコードをチェックした

# 6月26日
- 線形化の実装をした。メモリが破壊されたので疎行列表現にしてなんとかした
- 計算はできるようになったのだが、計算時間が爆発していたのでほっといた。結局局所最適解なんかを推していく形になると思う。

# 7月2日
- スライドの確認 (https://drive.google.com/file/d/1xe9vtNbDphGbW2lZ8_LZ7k1wXD6k8em5/view?usp=sharing)
- 現在までに完成したコード (https://drive.google.com/drive/folders/1-K2RxuPSJe0afatQ3-tFSw2nPdWrqHgE?usp=sharing)

# 7月10日
- 発表です
- https://drive.google.com/drive/folders/1-K2RxuPSJe0afatQ3-tFSw2nPdWrqHgE?usp=sharing にだいたい入ってます
