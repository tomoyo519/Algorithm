import sys
input = sys.stdin.readline

number = int(input())

arr = [ list(map(int,input().split())) for _ in range(number )]
arr.sort(key=lambda x:(x[1],x[0]))

# print(arr)
count = 1;
end_time = arr[0][1]

for i in range(1, number):
    if (arr[i][0] >=end_time):
        
        count +=1
        end_time = arr[i][1]
        
print(count)