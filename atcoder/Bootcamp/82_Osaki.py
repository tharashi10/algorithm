"""
Imos法
自力でACできた

3
05:47:15 09:54:40
12:12:59 12:13:00
16:30:20 21:18:53
6
00:00:00 03:00:00
01:00:00 03:00:00
02:00:00 03:00:00
03:00:00 04:00:00
03:00:00 05:00:00
03:00:00 06:00:00
0
--
1
3
"""

from itertools import accumulate
def main():
    while True:
        N=int(input())
        if N==0:
            return
        
        C = [0]*2*int(1e6)
        for i in range(N):
            s,t = map(str,input().split())
            ss=int(s[0:2])*3600 + int(s[3:5])*60 + int(s[6:8])
            tt=int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:8])
            C[ss]+=1
            C[tt]-=1

        C = list(accumulate(C))
        print(max(C))

if __name__=="__main__":
    main()
