N = int(input())
H = list(map(int,input().split()))

def completeBinaryTree(N,H):
    for i in range(N):
        if i==0:
            print(f'node {i+1}: key = {H[i]}, ',end='')
            print(f'left key = {H[1]}, ',end='')
            print(f'right key = {H[2]}, ',end='')
            print()
        else:
            # 親が存在している仮定の下(i>=1)
            j = i+1
            p_idx = j//2
            l_idx = j*2
            r_idx = j*2+1
            print(f'node {i+1}: key = {H[i]}, ',end='')
            print(f'parent key = {H[p_idx-1]}, ',end='')

            if l_idx <= N:
                print(f'left key = {H[l_idx-1]}, ',end='')
            
            if r_idx <= N:
                print(f'right key = {H[r_idx-1]}, ',end='')
            print()

completeBinaryTree(N,H)