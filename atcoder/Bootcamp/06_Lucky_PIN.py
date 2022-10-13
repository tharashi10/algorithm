""": Atcoder D - Lucky PIN
普通にfor ..for ..forで回すとTLEになる.
なかなか厄介.
Pointは、今回3桁指定なので[0-9][0-9][0-9]で最大1000個しかパターンがないということ
->したがって、000-999の中に全探索したものが含まれているかを調べればOK
-------
実行時間: 27 ms
"""

n=int(input())
s=str(input())
cnt = 0
for i in range(1000):
    v = str(i).zfill(3)
    p = s.find(v[0])
    if p!=-1:
        pp = s.find(v[1],p+1)
        if pp!=-1:
            ppp = s.find(v[2],pp+1)
            if ppp !=-1:
                cnt+=1
print(cnt)