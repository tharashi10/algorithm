"""
QuickSort
(Divide Conquer)
---
Input
6
D 3
H 2
D 1
S 3
D 2
C 1
---
Output
Not stable
D 1
C 1
D 2
H 2
D 3
S 3
"""

def partition(A,p,r):
def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

if __name__ == "__main__":
    n = int(input())
    M = map()
