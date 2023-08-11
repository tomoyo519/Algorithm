a = int(input())
b = int(input())
c = int(input())

result = a*b*c;
arr = list(str(result))
# 0부터 9까지 10개의 자리수
# arr = ['1','7'037300]
resultArr = [0,0,0,0,0,0,0,0,0,0]
for i in arr:
    for k in range(0,10):
        if(i == str(k)):
            resultArr[k] +=1;

for j in resultArr:
    print(j)
