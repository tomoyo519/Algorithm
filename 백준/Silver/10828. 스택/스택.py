import sys

number = int(sys.stdin.readline())
result = []
for i in range(number):
    command = list(map(str, sys.stdin.readline().split()))
    if(command[0] == "push"):
        result.append(int(command[1]))
    if(command[0] == "top"):
        if(len(result) > 0):
            print(result[-1])
        else:
            print("-1")
    if(command[0] =="size"):
        print(len(result))
    if(command[0] =="empty"):
        print("1" if len(result) ==0 else "0")   
    if(command[0] =="pop"):
        if(len(result )> 0):
            tmp = result.pop()
            print(tmp)
        else:
            print("-1")