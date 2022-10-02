"""ABC271
数列の問題(B)
結構速攻で解けた。8分くらい
Input
2 2
3 1 4 7
2 5 9
1 3
2 1
"""

N, q = map(int,input().split())
L = []
Q = []
for _ in range(N):
    ll = []
    ll = list(map(int,input().split())) 
    L.append(ll[1:])
for _ in range(q):
    qq = list(map(int,input().split()))
    Q.append(qq)

for i in range(len(Q)):
    L_idx = Q[i][0]-1
    L_jdx = Q[i][1]-1
    print(L[L_idx][L_jdx])
 