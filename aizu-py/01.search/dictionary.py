"""
Input()
6
insert AAA
insert AAC
find AAA
find CCC
insert CCC
find CCC
--------
Output()
yes
no
yes
"""

# findの場合Searchする
def search(dic, st):
    exists = False
    for j in range(len(dic)):
        #print(dic)
        if dic[j]==st:
            exists=True
            break
        else:
            continue
    if exists:
        print('yes')
    else:
        print('no')

def execute(n, X):
    my_dict = []
    for i in range(n):
        {my_dict.append(X[i][1]) if X[i][0]=="insert" else search(my_dict, X[i][1])}

if __name__ == "__main__":
    """: n=999997とかでやるとTEとなる（listが遅いため→Setで）
    n = int(input())
    commands = []
    for _ in range(n):
        command = list(input().split())
        commands.append(command)
    execute(n, commands)
    """
    d = set()
    for _ in range(int(input())):
        command, s = input().split()
        if command == "find":
            print("yes" if s in d else "no")
        else:
            d.add(s)
    #print(d)
