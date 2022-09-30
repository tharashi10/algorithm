"""
Priority Queue(優先度付きプライオリティキュー)
Input
insert 8
insert 2
extract
insert 10
extract
insert 11
extract
extract
end
-------
Output
8
10
11
2
"""

# 問題のTest CaseがPythonだと通らない説あり
# ヒープライブラリを使っている人のブログ等参照したが、通らなかった
# おそらくv1->v2になったタイミングでTest Caseが変わっている
from heapq import heappop, heappush

if __name__ == "__main__":
    heap = []
    while True:
        op = input()
        if op.startswith("end"):
            break
        if op.startswith("extract"):
            print(-heappop(heap))
        else:
            num = int(op.split()[1])
            heappush(heap, -num)

# N=9999 のテストでTLEとなるため、Heapモジュールを
#def proc_command(cmd, queue):
#    if cmd.startswith('insert'):
#        queue.append(int(cmd[7:]))
#    
#    if cmd.startswith("extract"):
#        #print(queue)
#        #print("MaxValue: %s." % max(queue))
#        output.append(max(queue))
#        queue.remove(max(queue))
#    
#    if cmd.startswith('end'):
#        return "end"
#
#if __name__ == "__main__":
#    queue = []
#    output = []
#    while True:
#        cmd = input()
#        if cmd=="end":
#            break
#        else:
#            proc_command(cmd, queue)   
#    [print(output[i]) for i in range(len(output))]
