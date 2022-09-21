"""
双方向連結リスト
Input()
7
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
-------
Output()
6 1 2

---
Inpute (2)
9
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
deleteFirst
deleteLast
--
Input : TODO
8
insert 1000000000
insert 999999999
deleteLast
insert 1234566890
insert 5
deleteFirst
insert 7
delete 5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNodeAtFirst(self, x):
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

    def deleteLast(self):
        if self.head is None:
            return
        else:
            cur = self.head
            while cur.next is not None:
                prev = cur
                cur = cur.next
            
            prev.next = None
            cur = None

    # TODO 見直し
    def deleteNode(self, x):
        if self.head is None:
            return
        else:
            cur = self.head
            # 先頭とマッチした場合
            if cur.data == x:
                self.head = cur.next 
                cur = None
                return
            else:
                # 先頭ではないものを消す場合
                while cur.next is not None:
                    if cur.data == x:
                        break
                    prev = cur
                    cur = prev.next
                # breakした後 cur が削除対象となる
                if cur is None: # Nodeがなかった場合
                    return
                
                # Node が見つかった場合, nextを上書く
                prev.next = cur.next
                return

    def printNode(self):
        cur = self.head
        while cur is not None:
            if cur.next is not None:
                print(cur.data, end=" ")
            else:
                print(cur.data)
            cur = cur.next

if __name__=="__main__":
    d = set()
    linkedList = LinkedList()

    for _ in range(int(input())):
        # 引数の個数が可変なので文字連結しちゃう
        # command, s = (input().split())

        # rstrip()で改行コードを取り除く
        command = input().rstrip()
        #print(command)
        if command[0] == "i":
            linkedList.insertNodeAtFirst(command[7:])
        elif command[6] == "F":
            linkedList.deleteAtFirst()
        elif command[6] == "L":
            linkedList.deleteLast()
        else :
            #command == "deleteFirst":
            linkedList.deleteNode(command[7:])
            
    linkedList.printNode()
