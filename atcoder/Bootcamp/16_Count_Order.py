"""
Count Order
・方針: index()関数を使ってみる
Input--
3
1 3 2
3 1 2
Output---
3

実行時間 : 31 ms
"""
import itertools

n = int(input())

p = tuple(list(map(int,input().split())))
q = tuple(list(map(int,input().split())))

ll = [i for i in range(1,n+1)]
pattern = list(itertools.permutations(ll))

d = abs((pattern.index(p)+1) - (pattern.index(q)+1))
print(d)