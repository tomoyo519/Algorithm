from collections import deque;

number = int(input())
result = deque()
for i in range(1, number+1):
    result.append(i)

while(len(result)>1):
    result.popleft()
    tmp = result.popleft()
    result.append(tmp)
print("".join(map(str, result)))