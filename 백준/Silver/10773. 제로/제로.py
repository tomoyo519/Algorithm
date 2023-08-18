number = int(input())
jangbu = []
for i in range(number):
    line = int(input())
    if(line == 0):
        jangbu.pop();
    else:
        jangbu.append(line)
        

print(sum(jangbu))