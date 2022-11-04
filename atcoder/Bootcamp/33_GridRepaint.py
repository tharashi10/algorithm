"""
方針:
・最短経路を求めて、経路以外で黒にしてもOKな箇所がスコアになるはず
・つまり、Score=(H*W)-(Blackのマス)-(最短ステップ数)

--Input--
3 3
..#
#..
...
--Score--
2
"""
h,w = map(int,input().split())
A = []
for _ in range(h):
    st = input()
    A.append([st[i]for i in range(w)])
print(A)