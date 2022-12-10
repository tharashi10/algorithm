# ALDS1_14_A
# Naive String Match
"""
Input: 
aabaaa
cc
Output:
0 
3 
4
"""
for i in range(2):
    if i ==0:
       str1 = input()
    else:
        str2 = input() 

cnt = 0
for i in range(0,len(str1)-len(str2)+1):
    if str1[i:i+len(str2)] == str2:
        print(i)
        cnt +=1
