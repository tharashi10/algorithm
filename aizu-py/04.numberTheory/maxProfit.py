def getMaxProfit(A):
    # minv: Aのこれまで出てきた数値の最小値
    # maxv: 得られる最大利益
    minv = A[0]
    maxv = A[1]-A[0]
    for j in range(1,len(A)):
        maxv =  maxv if A[j]-minv < maxv else A[j]-minv
        minv =  A[j] if minv > A[j] else minv
    print(maxv)

N = int(input())
l = [int(input()) for i in range(N)]

getMaxProfit(l)