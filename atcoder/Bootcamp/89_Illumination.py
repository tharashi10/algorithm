"""
RunLengthで解いてみる
(Brute-forse(部分点)の他、手が出ないので解説を)
https://www.ioi-jp.org/joi/2012/2013-ho/2013-ho-t1-review.pdf

・交互列の長さを数値化する
・最大3つ連続する部分の最大値がAns

10
1 1 0 0 1 0 1 1 1 0
--
7
"""

def main():
    N = int(input())
    ll = list(map(int,input().split()))
    alternate = []
    
    for i in range(N):
        if i == 0:
            before=ll[i]
            alternate.append(1)
            continue
        
        if before!=ll[i]:
            alternate[len(alternate)-1]+=1
        else:
            alternate.append(1)
        before = ll[i]
    #print(alternate)

    def get_max(ll):
        val = 0
        if len(ll)==1:
            return 1
        if len(ll)==2:
            return ll[0]+ll[1]
        for i in range(len(ll)-2):
            val = max(val,ll[i]+ll[i+1]+ll[i+2])
        return val
    
    on_max = get_max(alternate)
    off_max = max(alternate)
    if on_max >= off_max:
        print(on_max)
    else:
        print(off_max)

if __name__=="__main__":
    main()
