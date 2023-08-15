firstNum = int(input())
firstArr = list(map(int, input().split()))
secNum = int(input())
secArr = list(map(int, input().split()))
firstArr.sort()

def binary_search( findNum, firstArr, start, finish):
    if(start > finish):
        return 0
    mid = (start+ finish) //2
    if(firstArr[mid] == findNum):
        return 1
    elif firstArr[mid] > findNum:
        return binary_search(findNum, firstArr, start, mid-1)
    elif firstArr[mid] < findNum:
        return binary_search(findNum, firstArr, mid+1, finish )
    
for i in secArr:
    print(binary_search(i, firstArr, 0, (firstNum-1)))
    