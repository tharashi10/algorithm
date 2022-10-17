"""
D - 派閥
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
print(M)
for i in range(2**n):
    group = []
    for k in range(n):
        if (i >> k)&1:
            group.append(k+1)

    if len(group) <=1:
        cnt = max(1,cnt)
        continue
    
    # TODO
    for i in range(len(group)-1):
        for j in range(i+1,len(group)):
            #print(M[group[i]-1][group[j]-1])
            if M[group[i]-1][group[j]-1] == 0:
                break # 2重Loopを一気に抜け出すためにElse/Continueする
        else:
            print(cnt,len(group),(i,j))
            cnt = max(cnt,len(group))
            continue

print(cnt)

""" bit
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [5], [1, 5], [2, 5], [1, 2, 5], [3, 5], [1, 3, 5], [2, 3, 5], [1, 2, 3, 5], [4, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]]
"""