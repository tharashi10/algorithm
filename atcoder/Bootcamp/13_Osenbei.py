"""
第７回日本情報オリンピック 予選 E - おせんべい
2 5
0 1 0 1 0
1 0 0 0 1
---
方針
・裏返しによって煎餅は反転するだけ。
・ある一連の操作があったとしても順番に依存しない。
・ある特定の行や列を2回裏返すと元に戻る。
・「どの行をひっくり返すか」を固定してしまうことを考える。行の選択方法は 2H 通りある。
これらの行をあらかじめひっくり返してしまうことにする。
"""

h,w = map(int,input().split())
M = []
for i in range(h):
    M.append(list(map(int,input().split())))

result = 0
for i in range(2*h):
    for k in range(h):
        if (i>>k)&1:
            for j in range(w):
                if M[k][j] == 0:
                    M[k][j] = 1
                else:
                    M[k][j] = 0
    tmp = 0
    for i in range(w):
        a = 0
        for j in range(h):
            if M[j][i]==0:
                a+=1
        tmp += max(a,h-a)
    result = max(result,tmp)

print(result)
