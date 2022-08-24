import time

x,y = map(int,input().split())
def gcd(k):
    g_list = []
    for i in range(1,k+1):
        if k % i == 0:
            g_list.append(i)
        else:
            continue
    return g_list

start = time.time()
list_x = gcd(x)
list_y = gcd(y)
and_list = set(list_x) & set(list_y)
print(max(and_list))
end = time.time()
print(end - start)
