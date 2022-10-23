"""
Eight Queens Problems
・方針: 8!の順列を探索する
・例えば,(6, 0, 2, 7, 5, 3, 1, 4)とあったときに、
(0行目のQueenの配置列,1行目のQueenの配置列,2行目のQueenの配置列,3行目のQueenの配置列..)
と定義できる。なぜなら、縦横は攻撃範囲になるため同じ行および列にQueenが配置されることはないため。
・斜め判定は、サクッといかないので要熟考
→1次関数的に考える: [x+y が同じ] または [x-y が同じ]場合は、対角線上に乗ってしまうことを利用する
Input---
3
2 2
5 3
Output---
......Q.
Q.......
..Q.....
.......Q
.....Q..
...Q....
.Q......
....Q...
"""
import itertools

n = int(input())
q1 = list(map(int,input().split()))
q2 = list(map(int,input().split()))

patterns = list(itertools.permutations(range(8)))

for p in patterns:
    l = []
    if p[q1[0]] == q1[1] and p[q2[0]] == q2[1]:
        print(f"p : {p}") #(7, 6, 2, 5, 4, 3, 1, 0)
        
        #斜め判定[TODO]     
        
        for i in range(8):
            l.append(['.' if n!=p[i] else 'Q' for n in range(8)])

print(l)
