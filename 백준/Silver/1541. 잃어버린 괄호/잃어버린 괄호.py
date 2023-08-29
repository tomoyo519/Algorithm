# 매 순간 최적이라고 생각되는 경우를 선택하기..

# - 를 만났는데 다음 연산이 있으면 넘어가기?

import sys
input = sys.stdin.readline

line = str(input().rstrip())

arr = line.split('-');

sum = 0;
num = []

for i in arr:
    tmp = 0;
    plusTmp = i.split('+')
    for j in plusTmp:
        tmp += int(j);
    num.append(tmp)
    
result = num[0];
for k in range(1, len(num)):
    result -= num[k];
    
print(result)
        
# print('arr', arr)