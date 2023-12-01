import sys
input = sys.stdin.readline
# a b c d

from collections import deque
words =list(input()[:-1])
stack = deque();

count = int(input()); # 4

for _ in range(count):
    order = input().split()
    if order[0] == 'L' and words:
        stack.appendleft(words.pop())
    elif order[0] == 'D' and stack:
        words.append(stack.popleft())
    elif order[0] == 'B' and words:
        words.pop()
    elif order[0] == 'P':
        words.append(order[1])

for values in words:
    print(values,end='')
for values in stack:
    print(values,end='')