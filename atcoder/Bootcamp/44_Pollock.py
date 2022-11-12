"""
ポロック予想
Input--
40
14
5
165
120
103
106
139
0
Output--
2 6
2 14
2 5
1 1
1 18
5 35
4 4
3 37

dp[i][j] := i番目までの数を使うとして、和がjとなる場合の正四面体の最小個数
odd[i][j] :奇数のみ計算に使う場合 

正四面体の個数
m=0,cal(m)=0
m=1,cal(m)=1
m=2,cal(m)=4
m=3,cal(m)=10
m=4,cal(m)=20
m=5,cal(m)=35
m=6,cal(m)=56
m=7,cal(m)=84
m=8,cal(m)=120
m=9,cal(m)=165

dp[使う数の個数][狙う和]
|-縦は和------------------
| 0 0 0 0 0 0 0 0 0 0  <- この行では何も使わないので当然0
| 1 2 3 4 5 6 7 8 9 10 <- m=1のみ使うとき、1(1個),1+1(2個),1+1+1(3個)....
| 1 2 3 1 2 3 4 2 3 4  <- m=1とm=4のみ使う. ex.狙う和が8なら、4+4(2個)
| 0 0 0 0 0 0 0 0 0 0  <- m=1,m=4,m=10を使う.
| 0 0 0 0 0 0 0 0 0 0  
--------------------
"""