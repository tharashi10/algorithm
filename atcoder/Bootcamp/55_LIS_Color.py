"""
LISの双対問題
色塗り
5
2
1
4
5
3
---
2
https://drken1215.hatenablog.com/entry/2020/12/25/184700
"""

import bisect
def main():
    N = int(input())
    seq  = [int(input()) for _ in range(N)]

    seq = seq[::-1] # 反転させる
    LIS = [float('inf') for _ in range(N)]
    #LIS[0] = seq[0]
    for i in range(N):
        if LIS[i]< seq[i]:
            LIS.append(seq[i])
        else:
            idx = bisect.bisect(LIS,seq[i]) # bisect_rightの働き
            LIS[idx] = seq[i]  
    print(bisect.bisect_left(LIS,float('inf')))

if __name__ =="__main__":
    main()
