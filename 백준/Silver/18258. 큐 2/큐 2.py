import sys
from collections import deque;
input = sys.stdin.readline
number = str(input())
result = deque()

for i in range(int(number)):
    command = list(map(str, input().split()))
    if(command[0] =="push"):
        result.append(command[1])
    elif(command[0] == "front"):
        if((len(result)) > 0):
            # tmp = result.popleft()
            # print(tmp)
            print(result[0])
        else:
            print("-1")
    elif(command[0] == "back"):
        if((len(result))> 0):
            # tmp = result.pop()
            print(result[-1])
        else:
            print("-1")
    elif(command[0] =="pop"):
        if(len(result) > 0):
            tmp = result.popleft()
            print(tmp)
        else:
            print("-1")
    elif(command[0] =="size"):

            print(len(result))
      
    elif(command[0] =="empty"):
        if(len(result) ==0):
            print("1")
        else:
            print("0")