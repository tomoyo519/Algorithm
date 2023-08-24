import sys
input = sys.stdin.readline

stringArr = input().rstrip()
stack = [False, False, False]

for i in range(len(stringArr)):
    if(stringArr[i] == 'P'):
        if(stack[-3] == 'P' and stack[-2]=='P' and stack[-1] =='A'):
            stack.pop()
            stack.pop()
            stack.pop()
    stack.append(stringArr[i])


if (''.join(stack[3:]) =='P'):
        print("PPAP")
else:
        print("NP")
