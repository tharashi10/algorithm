"""
文字列検索
Input---
aabaaa
aa
Output---
0
3
4
"""

str1 = input()
str2 = input()
for i in range(0,len(str1)-len(str2)+1):
    if str1[i:i+len(str2)]==str2:
        print(i)
