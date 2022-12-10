""":
Stringに含まれるかの判定
Input-----
aabaaa
4
aa
ba
bb
xyz
Output---
1
1
0
0
"""

# 以下だとTLEになる
str1 = str(input())
for i in range(int(input())):
    s = str(input())
    flg = 0
    for j in range(0,len(str1)-len(s)+1):
        if str1[j:j+len(s)]==s:
            print('1')
            flg += 1
            break
    if flg == 0:
        print('0')
