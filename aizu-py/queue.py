''':Queue
CPUの処理（クオンタム）
ラウンドロビンスケジューリング
入力
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
-----
出力
p2 180
p5 400
p1 450
p3 550
p4 800
プロセスが完了した順に、各プロセスの名前と終了時刻を空白で区切って１行に出力してください。
'''
class CpuQueue:
    def __init__(self, head, tail, max, q):
        self.head = head
        self.tail = tail
        self.max = max
        self.q = q

    def isEmpty(self):
        return self.head==self.tail

    def isFull(self):
        # 空である場合と区別するために、あと一個追加したらFullになってしまう状態をTrueで返す
        return self.head==(self.tail+1)%(self.max)

    def enqueue(self, x):
        if self.isFull():
            print("Will be Overflow...(cannot push)")
        self.q[self.tail] = x
        if self.tail+1 == self.max:
            self.tail = 0 # リングバッファ想定なので循環させる
        else:
            self.tail+=1
    
    def dequeue(self):
        if self.isEmpty():
            print("Will be Underflow...(cannot pop)")
        x = self.q[self.head]
        if self.head+1 == self.max:
            self.head = 0 # リングバッファ想定なので循環させる
        else:
            self.head+=1
        return x

def solver():
    n,t = map(int,input().split())
    m = 1000
    queue = [[]]* m
    for i in range(n):
        a,b = input().split()
        queue[i] = [a,int(b)]
    cq = CpuQueue(head=0, tail=n, max=m, q=queue)
    quant = 0
    #print('-----')
    while(not cq.isEmpty()):
        tmp = cq.dequeue()
        if tmp[1] > t: # Process完了しない場合
            tmp[1]-=t
            cq.enqueue(tmp)
            quant += t
        else: # Process完了する場合
            quant += tmp[1]
            print(tmp[0], quant)

if __name__ == "__main__":
    solver()