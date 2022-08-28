'''線形探索アルゴリズム
番兵法利用
'''
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

def linearSearch(key,searched_lst):
    i = 0
    searched_lst.append(key)
    while(not(searched_lst[i]==key)):
        i+=1
    if i==(len(searched_lst)-1):
        #print('Reached.')
        return "NotExists"
    return i

cnt = 0
for j in range(0,m):
    if not linearSearch(B[j],A)=='NotExists':
        cnt+=1
print(cnt)