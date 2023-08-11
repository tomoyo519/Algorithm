a, b = map(int, input().split())
arr = input().split()
result = []
count = 0
    
for i in arr:
    if(int(i)<b):
        result.append((i));
        count +=1
        
        
print(" ".join(result))