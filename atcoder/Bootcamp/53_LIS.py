"""
Longest Increasing Subsequence
LIS[i]:= 長さ i の単調増加部分列の右端の数字のうち、最小の値
https://kyoroid.github.io/algorithm/dynamic_programming/lis.html
5
5
1
3
2
4
---
3
"""
import bisect

def main():
    N = int(input())
    seq = [int(input()) for _ in range(N)]
    
    LIS = [seq[0]]    # 単調増加の文字列を作ろう、というモチベ
    for i in range(N):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i]) # 最後のやつよりも大きければ追加
        else:
            idx = bisect.bisect_left(LIS,seq[i])
            LIS[idx]=seq[i] # ex. [1,3,5]の時に、[2]をAppendして、[1,2,5]になる

    print(len(LIS))
    print(LIS)

if __name__=="__main__":
    main()
