"""
Longest Common Subsequence:最長共通部分列
左から順に文字を抜き出したときに、一致する部分列
→[注意]ALDSの問題でサブミットするとTLEになった。
→想定解法なのでOK
→もし、どうしても通したい場合はmax関数(遅い)を使わない等する必要あり

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
import copy

n = int(input())
s1 = []
s2 = []
for i in range(n):
    s1.append(input())
    s2.append(input())

dp_ = []

for i in range(1000):
    tmp = [0]*(1000)
    dp_.append(tmp)

for idx in range(n):
    str1 = s1[idx]
    str2 = s2[idx]
    dp = copy.copy(dp_)

    for k in range(len(str2)):
        for l in range(len(str1)):
            if str2[k]==str1[l]:
                dp[k+1][l+1] = dp[k][l]+1
            else:
                dp[k+1][l+1] = max(dp[k+1][l],dp[k][l+1])
    
    print(dp[len(str2)][len(str1)])
