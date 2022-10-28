"""
Darts
方針
・４本のダーツを加算した２本ずつに分ける(N^4の計算を回避できる)
・更なるペアを作る際に、Diffを二分探索をして、あたりをつけていく(logNの計算に持っていける)
・set()でMLEになったので、in Listでも早い場合もあることに留意すべし

Input--
4 50
3
14
15
9
Output--
48
"""

import bisect
import time
start = time.time()

n,m = map(int,input().split())
l = [0]
for i in range(n):
    l.append(int(input()))

ll = []
for i in l:
    for j in l:
        ll.append(i+j)

score = 0
ll.sort()

## ここをset(ll)にするとMLEとなる。set()でコストかかる説あり
for k in ll:
    if k > m:
        break
    tmp_id = bisect.bisect(ll,m-k)-1
    tmp_score = k + ll[tmp_id]
    score = max(score, tmp_score)

print(score)
end = time.time()
print(f"Exec Time: {end-start} [ms]") #Exec Time: 1.0306408405303955 [ms]