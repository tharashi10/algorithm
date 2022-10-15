"""Exhaustive Search
Bit全探索
bitシフトが有効になる
0または1で2乗分だけパターンがある
そのため、Nが小さければ全パターンを計算することができる

---In
5
1 5 7 10 21
4
2 4 17 8
---Out
no
no
yes
yes

実行時間:04:83 s (多分テストケースの合計)
"""

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

tt = set()
for i in range(2**n):
    t = 0
    for k in range(n):
        if (i >> k) & 1:
            t += A[k]
    tt.add(t)

for j in range(m):
    if B[j] in tt:
        print("yes")
    else:
        print("no")
