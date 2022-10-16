"""
C - Switches
---input
2 2
2 1 2
1 2
0 1
---output
1
"""

n,m = map(int,input().split()) # n:電球 , m:スイッチ
l = [] # lは、電球が繋がっているスイッチの個数
s = [] # sは、電球が繋がっているスイッチのID
#p = [] # pは、点灯条件に関わる値

for i in range(m):
    tmp=list(map(int,input().split())) #一回全部リストに詰め込む
    l.append(tmp[0])
    s.append(tmp[1:])

p = list(map(int,input().split()))

sum_cnt=0
ans = 0
for i in range(2**n):
    for j in range(m): # 全Switchを探索
        on_cnt = 0
        for g in range(l[j]): #あるSwitch jに対して接続されている電球を調べる
            if (i>>(s[j][g]-1))&1:
                on_cnt+=1
        
        if on_cnt%2 ==p[j]:
            sum_cnt +=1
            #print(bin(i))
    if sum_cnt == m:
        ans +=1

print(ans)