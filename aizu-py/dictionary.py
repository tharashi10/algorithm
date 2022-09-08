N = int(input())
commands = []
for _ in range(N):
    command = list(input().split())
    commands.append(command)

def search(dict, x):
    exists=False
    for j in range(len(dict)):
        if dict[j]==x:
            exists=True
            break
        else:
            continue
    if exists:
        print('yes')
    else:
        print('no')

def execute(N,X):
    my_dict = []
    for i in range(N):
        {my_dict.append(X[i][1]) if X[i][0]=="insert" else search(my_dict,X[i][1])}

execute(N,commands)
