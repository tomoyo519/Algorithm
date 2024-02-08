from collections import deque

def solution(s):
    data = deque(s)
    stack = deque()
    
    while data:
        current = data.popleft()
        if stack and stack[-1] == '(' and current == ')':
            stack.pop()
        else:
            stack.append(current)

    if len(stack) == 0:
        return True;
    else:
        return False
        
        
