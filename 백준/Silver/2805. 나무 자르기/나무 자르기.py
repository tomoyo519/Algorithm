
treeNum, needNum = map(int, input().split())
treeArr = list(map(int, input().split()))
#10 15 17 20
# 7 
start, end = 1, max(treeArr)

while (start<=end):
    mid = (start + end) //2
    log =0 
    for i in treeArr:
        if(i >= mid):
            log += (i-mid)
    if(log >= needNum):
        start = mid+1
    else:
        end = mid -1     
print(end)
