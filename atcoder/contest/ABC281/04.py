"""
itertoolsのCombination使うとTLEになる
4 2 2
1 2 3 4
"""
from itertools import combinations

def main():

    N,K,D = map(int,input().split())
    ll = list(map(int,input().split()))
    su = {sum(x) for x in set(combinations(ll,K))}
    ref = {i*D for i in range(len(su))}
    #even_list = list(filter(lambda x: not x%D,su))
    even_set = su & ref
    if len(even_set)==0:
        print(-1)
    else:
        print(max(even_set))

if __name__=="__main__":
    main()
