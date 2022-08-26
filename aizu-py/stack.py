'''逆ポーランド記法
reverse polish notation
'''
input = list(map(str,input().split()))
def reversedPollish(list):
    stack = []
    for i in range(0,len(input)):
        if input[i] =='+':
            x,y = stack.pop(),stack.pop()
            stack.append(y+x)
        elif input[i] =='-':
            x,y = stack.pop(),stack.pop()
            stack.append(y-x)
        elif input[i] =='*':
            x,y = stack.pop(),stack.pop()
            stack.append(x*y)
        elif input[i] =='/':
            x,y = stack.pop(),stack.pop()
            stack.append(y/x)
        else:
            stack.append(int(input[i]))
    print(*stack)

reversedPollish(input)