"""
碁石ならべ
ランレングス圧縮する(連長圧縮)
decode/encodeの実装はPythonでList(tuple(char,int))使って簡単にできる

0=White
1=Black
8
1
0
1
1
0
0
0
0

PC再起動のためブラウザメモ
https://docs.python.org/3/library/itertools.html#itertools.groupby
https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_accessibility
https://spring.io/guides/tutorials/react-and-spring-data-rest/
https://atug.tokyo/?p=490
https://cstack.github.io/db_tutorial/parts/part5.html
https://www.youtube.com/watch?v=oLO7kLNJt7A
"""
from itertools import groupby
def main():
    N= int(input())
    st = ""
    for _ in range(N):
        st+=(str(input()))
    
    print(f"st={st}")

    def decode_runlength(ll:"List(())")->str:
        s = ""
        for c, num in ll:
            s+=c*int(num)
        return s

    def encode_runlength(s:str)->"List(tuple(str,int))":
        g = groupby(s) # iterator
        A = []
        for k,v in g:
            A.append((k,len(list(v))))
        return A
    
    print(encode_runlength(st))
    
    # Even または Oddで場合分け


if __name__=="__main__":
    main()
