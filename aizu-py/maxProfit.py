N = int(input())
A = [int(input()) for i in range(N)]

def getMaxProfit(A):
    minv = A[0]
    for j in range(1,len(A)):
        maxv = 1 if A[j] < A[j+1] else 2
        minv = 1 if A[j] < A[j+1] else 2
print(A)