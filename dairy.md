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
-- 立ち見のスペースを先に確保しておいて、0-1変数で管理する
- 貪欲なアルゴリズム（?）と最適解を比較しても楽しそう→計算量は大丈夫？
- 距離に反比例する効用と、比例する効用をどうバランスよく加味するか
- https://docs.google.com/document/d/1QpkhLUOC5uwh314LF24qTn6gN6xwJDB1UmntduA_CNU/edit (定式化 by東田)
- 順番に座っていくのを考えると、逐次最適化の方が向いているかも…? (by川合)
- 項目ごとでなくて、何を一番優先するかの情報が大切そう(by東田)
- 仲良い人と隣になる→制約条件として定式化できそう
-- https://drive.google.com/file/d/1p6NLHphOT0vy0hiE4TTaqnxMUj5hR3EG/view (by大中)
- 定式化について色々まとめてみた(by 佐藤)
-- https://docs.google.com/document/d/1HS_pr-34JD3IUTi1D-M_yShCIn3wknpK2a3tEDoP_iE/edit
-- 参考: https://www.slideshare.net/MikioKubo/gurobi-python
