"""
Average Length
・方針: itertoolsのPermutaions(array)を利用する
・出力形式は適当でも通る(桁数を合わせる必要ない)
----
Input
----
3
0 0
1 0
0 1
---
OutPut : 2.276142374915397
---
実行時間: 460 ms
"""

import itertools
import math

n = int(input())
l = []
for _ in range(n):
    l.append(tuple(map(int,input().split())))

pattern = list(itertools.permutations(l))

dist =0
for ptn in pattern:    
    for i in range(n-1): #ptn=((0, 0), (1, 0), (0, 1))
        dx = ptn[i][0]-ptn[i+1][0]
        dy = ptn[i][1]-ptn[i+1][1]
        d = math.sqrt(dx**2+dy**2)
        dist+=math.sqrt(dx**2+dy**2)

ave_d = dist/len(pattern)
print(f"{ave_d}")