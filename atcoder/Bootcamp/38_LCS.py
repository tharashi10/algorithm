"""
Longest Common Subsequence:最長共通部分列
左から順に文字を抜き出したときに、一致する部分列
3
abcbdab
bdcaba
abc
abc
abc
bc
--
4
3
2
"""
n = int(input())
s1 = []
s2 = []
for i in range(n):
    s1.append(input())
    s2.append(input())

for idx in range(n):
    dp = []
    str1 = s1[idx]
    str2 = s2[idx]
    
    for i in range(len(str2)+1):
        tmp = [0 for j in range(len(str1)+1)]
        dp.append(tmp)

    for k in range(len(str2)):
        for l in range(len(str1)):
            if str2[k]==str1[l]:
                dp[k+1][l+1] = dp[k][l]+1
            else:
                dp[k+1][l+1] = max(dp[k+1][l],dp[k][l+1])
    
    print(dp[len(str2)][len(str1)])

