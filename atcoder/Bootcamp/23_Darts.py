"""
Darts
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

n,m = map(int,input().split())
l = [0]
for i in range(n):
    l.append(int(input()))

ll = []
for i in l:
    for j in l:
        ll.append(i+j)

ll.sort()
score = 0
for k in set(ll):
    if k > m:
        break
    dif = m-k
    tmp_id = bisect.bisect(ll,dif) -1
    tmp_score = k + ll[tmp_id]
    score = max(score, tmp_score)

print(score)