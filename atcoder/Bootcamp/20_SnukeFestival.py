"""
Snuke Festival
方針: [NG]上段/中段の組み合わせ(i,j)を作り、
      下段に対してBisect(二分探索)してみる
      [OK]「中段」を固定する
      → 中段を固定して、上段と下段をbisectする
      計算量的に[NG]の方がTLEになっちゃう
-----
Input
2
1 5
2 4
3 6
Output
3
"""

import bisect

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

cnt = 0
# BをSetにするとNG(理由: B=[3 3 3]の時にB=[3]となり、TestCase2が合わなくなるため)
for b in B:
    a_id = bisect.bisect_left(A,b)
    c_id = bisect.bisect_right(C,b) # rightにするのは、検索値とリスト値が同じ場合にそれを弾きたいから
    cnt+=(a_id*(len(C)-c_id))
    print(f"b={b}: {a_id*(len(C)-c_id)}")

print(cnt)
