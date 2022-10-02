"""ABC271
16進数問題(A)
時間かけてしまった。For文内でl[z]をl[r]と書いていて、
TREとなるのを解消するのに予想外に時間を費やした
"""

N = int(input())
l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
r = N%16
z = N//16
if N>=16:
    if str(z) in ['0','1','2','3','4','5','6','7','8','9']:
        if str(r) in ['0','1','2','3','4','5','6','7','8','9']:
            print(f'{z}{r}')
        else:
            alp = l[r]
            print(f'{z}{alp}')
    else:
        if str(r) in ['0','1','2','3','4','5','6','7','8','9']:
            alp1 = l[z]
            print(f'{alp1}{r}')
        else:
            alp1 = l[z]
            alp2 = l[r]
            print(f'{alp1}{alp2}')
else:
    if str(N) in ['0','1','2','3','4','5','6','7','8','9']:
        print(f'0{N}')
    else:
        alp = l[N]
        print(f'0{alp}')
 