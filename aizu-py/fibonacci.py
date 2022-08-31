"""再帰法
動的計画法=「漸化式」+「解の保存」
a_n= a_n-1 + a_n-2
"""
import time
def fibonacci(n):
    if n<=1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
start = time.time()
print(fibonacci(30))
end = time.time()
print(end-start)
