number = int(input()) # 5
numArr = list(map(int, input().split())) # 6 9 5 7 4

result = []
stack = []
for i, num in enumerate(numArr):
    while stack:
        if(stack[-1][1] > num): # 수신 가능
            result.append(stack[-1][0] + 1)
            break;
        else:
            stack.pop()
    if not stack:
        result.append(0)
        
    stack.append((i, num))

print(" ".join(map(str,result)))