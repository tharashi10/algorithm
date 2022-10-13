""":
"""

import re
n=int(input())
s=str(input())

sets=set()
index_lst=[i for i in range(n)]

if (n-3)==1:
    for i in index_lst:
        sets.add(s[:i]+s[i+1:])
        print(len(sets))

if (n-3)==2:
    for i in index_lst:
        index_lst.remove(i)
        ss = s[:i]+'N'+s[i+1:]
        for j in index_lst:
            sss = ss[:j]+'N'+ss[j+1:]
            sets.add(sss.replace('N',''))

if (n-3)==3:
    for i in range(len(index_lst)-2):
        ss = s[:i]+'A'+s[i+1:]
        for j in range(i+1,len(index_lst)-1):
            sss = ss[:j]+'B'+ss[j+1:]
            for k in range(j+1,len(index_lst)):
                ssss = sss[:k]+'C'+sss[k+1:]
                sets.add(re.sub(r'[A-C]','',ssss))

if (n-3)>3:
    for i in range(len(index_lst)-2):
        ss = s[i]
        for j in range(i+1,len(index_lst)-1):
            sss = s[j]
            for k in range(j+1,len(index_lst)):
                ssss = s[k]
                st = ss+sss+ssss
                sets.add(st)

print(len(sets))