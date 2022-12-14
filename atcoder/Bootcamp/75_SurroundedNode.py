"""
F: Number of Surrounded Nodes
難易度的に一旦SKipする。
いけそうな気はするが、先に累積和を倒すこととする

辺に着目した場合、
・ans=(部分木Sの頂点の個数)-(黒く塗られた頂点の個数)
・(黒く塗られた頂点の個数)=確率1/2で全頂点N個なので 期待値 N/2個
・(部分木Sの頂点の個数)=Sに含まれる辺の個数+1

・全体木Tから、エッジeを取り除いてできる二つの部分木A,Bの両方に、
黒く塗られた頂点が存在する=エッジeは部分木Sに含まれる

・確率 = (1-(1/2)^p) * (1-(1/2)^(N-p))
p: 部分木Aに含まれる頂点の個数 上の式は少なくとも一つ黒い頂点が含まれる確率の掛け算

・各辺eに対して、pを計算すれば、「Sに含まれる辺の個数」がもとまる。
DFSを利用する

https://atcoder.jp/contests/abc149/submissions/9241604
https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92
"""