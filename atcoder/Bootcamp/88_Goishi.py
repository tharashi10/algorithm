"""
碁石ならべ
ランレングス圧縮する(連長圧縮)
decode/encodeの実装はPythonでList(tuple(char,int))使って簡単にできる

めちゃめちゃ粘ってACできた。時間かかった。
時間がかかった部分は、listのRemoveのところ。末尾を消す意図で
list.remove(len(list),(color,int))のようにしていたけど、
どうしてもListの順序が途中で変わってしまって、最後のElse文のところで2個前が正しく参照できていなかった。
→そのため、removeではなく、pop()で消すようにしたところ上手くいった。
→remove/insertのように、indexを指定して消す/追加する時は気をつけたほうがいい。

あと、RunLengthのメソッドを今回は使ってないが、備忘として残しておく

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
    
    # Same Color または Different Color で場合分け
    ll = []
    ll.append((str(input()),1))
    for i in range(N-1):
        color = str(input())
        atLast = ll[-1]

        # Same Color
        if atLast[0] == color: # 4th/6th/7th/8th
            ll.pop()
            ll.append((color,atLast[1]+1))

        # Different Color
        elif i%2==1: # Odd 3rd/5th
            ll.append((color,1)) #奇数ならイロチでも塗り替えはしない
            
        elif len(ll)==1: # 2nd
            # イロチかつ偶数
            # 新規に置く碁石の色で塗り替える
            ll.pop()
            ll.append((color,atLast[1]+1))
            
        else:
            atSecondLast = ll[-2]
            ll.pop()
            ll.pop()
            ll.append((atSecondLast[0],atLast[1]+atSecondLast[1]+1))
            
        #print(f"*** {i+2}th : ll={ll} ***")
    ans = 0
    for i in range(len(ll)):
        if ll[i][0]==str(0):
            ans+=ll[i][1]
    print(ans)

if __name__=="__main__":
    main()
