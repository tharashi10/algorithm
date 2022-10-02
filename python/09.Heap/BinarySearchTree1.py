"""
BinarySearchTree;二分探索木
Input()
-------
8
insert 30
insert 88
insert 12
insert 1
insert 20
insert 17
insert 25
print
-------
 1 12 17 20 25 30 88
 30 12 1 20 17 25 88
""""

class Node:
    def __init__(self,parent,right,left):
        self.parent = parent
        self.right = right
        self.left = left

def insert(Tree, z):
    y = None
    x = Tree[0]
    while x != None:
        y = x
        if z.key < y.key:
            x = x.left
        else:
            x = x.right
    z.parent = y

    # Treeが空
    if y == None:
        Tree[0] = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def print():


if __name__ == "__main__":
    n = input()
    T = []
    for i in range(n):
        s = str(input())
        if s.startwith("insert"):
            insert(T, s[7:])
        else:
            print()