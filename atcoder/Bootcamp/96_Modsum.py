"""
ex. 5
X%1=0
X%2=1
X%3=2
X%4=3
X%5=4
--> max modsum=10
n-1個までの総和がAns
13
--
78
"""
def main():
    N=int(input())
    ans = (N-1)*(N)//2
    print(ans)

if __name__=="__main__":
    main()
