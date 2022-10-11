"""ABC122: B - ATCoder
英大文字からなる文字列 S が与えられます。
S の部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。
In: ATCODER
Out: 3
実行速度:25 ms
"""

s = str(input())
ACGT_lst = ['A','C','G','T']
lst = []

for i in range(len(s)):
    if s[i] in ACGT_lst:
        lst.append(1)
    else:
        lst.append(0)

for i in range(len(lst)-1):
    if lst[i+1]==1:
        lst[i+1] +=lst[i]
print(max(lst))
