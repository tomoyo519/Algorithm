number, deleteNum = map(int, input().split())
from collections import deque;
peopleArr = deque()
result = []

for i in range(1, number +1):
    peopleArr.append(i)

while(True):
    if(len(peopleArr) ==0):
        break;
    for i in range(0, deleteNum): # 0,1,2
        if(deleteNum - 1 == i):
            tmp = peopleArr.popleft()
            result.append(tmp)
        else:
            tmp = peopleArr.popleft()
            peopleArr.append(tmp)
            
            
dap1 = []
for i in result:
    dap1.append(str(i))
dap2 = ", ".join(dap1)
print('<'+dap2+'>')