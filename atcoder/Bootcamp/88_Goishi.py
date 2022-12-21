"""
碁石ならべ
ランレングス圧縮する(連長圧縮)
decode/encodeの実装はPythonでList(tuple(char,int))使って簡単にできる

0=White
1=Black
-------
8
1
0
1
1
0
0
0
0
--
6
"""
from itertools import groupby

def main():
    N= int(input())

    #基本 Method
    def decode_runlength(ll:"List(())")->str:
        s = ""
        for c, num in ll:
            s+=c*int(num)
        return s
    
    #基本 Method
    def encode_runlength(s:str)->"List(tuple(str,int))":
        g = groupby(s) # iterator
        ll = []
        for k,v in g:
            ll.append((k,len(list(v))))
        return ll
    
    # Even または Odd で場合分け
    ll = []
    for i in range(N):
        if i==0:
            ll.append((str(input()),1))
            continue
        
        color = str(input())
        atLast = ll[-1]
        
        # Same Color
        if atLast[0] == color:
            ll.remove(atLast)
            ll.insert(len(ll),(atLast[0],atLast[1]+1))
        else:
            # Different Color
            if i%2==1: # Odd
                ll.append((color,1))
            else:
                # 新規に置く碁石の色で塗り替える
                ll.remove(atLast)
                ll.insert(len(ll),(color,atLast[1]+1))
    ans = 0
    for i in range(len(ll)):
        if ll[i][0]==str(0):
            ans+=ll[i][1]
    print(f"ll={ll}")
    print(ans)

if __name__=="__main__":
    main()
