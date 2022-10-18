"""
D - 派閥
ポイント
(1)探索パターンを出して、それを派閥用グループと照らし合わせる
(2)知り合いかどうかをCHeckする際に、2つ選び出す工程があるが、For..Forでi,jを使えばOK
(3)条件から外れ、2重ループを一気に抜け出したい時は、Flagを使うべし(Else/Continueはわかりづらい)
---Input
5 3
1 2
2 3
1 3
---Output
3
"""

n, m = map(int,input().split())
M = [[0]*n for _ in range(n)]
for i in range(m):
    s,t = map(int,input().split())
    s_idx, t_idx = s-1,t-1
    M[s_idx][t_idx] = 1
    M[t_idx][s_idx] = 1

cnt = 0
for i in range(2**n):
    group = []
    for k in range(n):
        if (i >> k)&1:
            group.append(k+1)
    #print(group)
    if len(group) <=1:
        cnt = max(cnt,1)
        continue
    
    # Bit探索パターンをGroup(派閥)配列と照らし合わせてCheckする
    flag = False
    for i in range(len(group)-1):
        for j in range(i+1,len(group)):
            if M[group[i]-1][group[j]-1] == 0:
                flag = True
                break # 2重Loopを一気に抜け出すためにElse/Continueする
        if flag:
            break
    if not flag:
        cnt = max(cnt,len(group))

print(cnt)

""" bit: 全パターン n=3の時
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [5], [1, 5], [2, 5], [1, 2, 5], [3, 5], [1, 3, 5], [2, 3, 5], [1, 2, 3, 5], [4, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]]
"""