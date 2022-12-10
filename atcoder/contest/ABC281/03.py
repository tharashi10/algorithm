"""
3 600
180 240 120
"""
from itertools import accumulate
import bisect

N,T = map(int,input().split())
ll = list(map(int,input().split()))

x = T%(sum(ll))
cum  = [0] + list(accumulate(ll))
idx = bisect.bisect_left(cum,x)
print(idx,x-cum[idx-1])
