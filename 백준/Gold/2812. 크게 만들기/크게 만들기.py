import sys
input = sys.stdin.readline

number, deleteNum = map(int,input().split())
numArr = input().strip()

result = []

for num in numArr:
    while deleteNum > 0 and result:
        if(result[-1] < num): # 4 1,9,4 2 ,4 4 ,4
            result.pop()
            deleteNum -=1
        else:
            break;
    result.append(num)
    
if deleteNum > 0:
    print("".join(result[:-deleteNum]))
else:
    print("".join(result))