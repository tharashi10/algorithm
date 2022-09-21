"""
双方向連結リスト
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, x):
        if self.head is None:
            newNode = Node(x)
            self.head = newNode
        else:
            newNode = Node(x)
            newNode.next = self.head
            self.head = newNode # headを更新

    def deleteAtFirst(self):
        if self.head is None:
            print("The linked list empty. Cannot delete an element.")
            return
        else:
            node = self.head
            self.head = self.head.next
            del node

    # TODO
    def deleteNode(self, x):
        if self.head is None:
            return
        else:
            cur = self.head
            while cur is not None:
                if cur.next is None:
                    print("Cur.next is None.")
                    cur = None
                elif cur.next.data == x:
                    del cur.next
                    cur.next = cur.next.next #delした分ポインタを更新する
                    cur = cur.next
                    break
                else:
                    cur = cur.next

    def printNode(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end="")
            cur = cur.next
            
if __name__=="__main__":
    d = set()
    linkedList = LinkedList()
    for _ in range(int(input())):
        command, s = input().split()
        if command == "insert":
            linkedList.insertNode(s)
        if command == "delete":
            linkedList.deleteNode(s)
    linkedList.printNode()
    #
    #if command == "deleteFirst":
    #if command == "deleteLast":