import sys
import math
input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().split()))

arr.sort();

left , right = 0, num -1;
result = math.inf
resultArr = []

#조건 다시 확인 가능
while(left < right):
    
    sumsum = arr[left] + arr[right]
    if(abs(sumsum) < abs(result)):
        result = sumsum;
        resultArr = [ arr[left], arr[right ] ]
        
    if(result ==0):
        # 종료조건
        result = sumsum;
        resultArr = [ arr[left], arr[right ] ]
        break;
    
    if(sumsum < 0):
        left +=1;
    else:
        right -=1;
        
print(resultArr[0], resultArr[1])