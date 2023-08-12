number = int(input());
count = 0;
arr = list((input().split()));

for j in arr:
           semicount = 0;
           for i in range(1,int(j)+1):
               if(int(j) % i ==0):
                   semicount += 1;
           if(semicount ==2):
               count +=1
           
print(count)