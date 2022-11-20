"""
トランプ挿入ソート

https://www.slideshare.net/chokudai/abc006
上記のスライドP45からのGIFで、LISをわかりやすく説明している

#53と同じ解き方
6
1
3
5
2
4
6
--
2
"""
import bisect

def main():
    N = int(input())
    seq = [int(input()) for _ in range(N)]

    LIS = [seq[0]]
    for i in range(N):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            idx = bisect.bisect_left(LIS,seq[i])
            LIS[idx] = seq[i]
    
    print(N-len(LIS))

if __name__=="__main__":
    main()
