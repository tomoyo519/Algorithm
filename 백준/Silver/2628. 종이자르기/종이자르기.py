garo, sero = map(int, input().split())
num = int(input())
row = [0, garo]
column = [0, sero]

for i in range(0, num):
    cutG, cutS = map(int, input().split())
    if(cutG == 0):
        column.append(cutS) # [ 0, 3,  8]
    else:
        row.append(cutS) # [ 0, 4, 10]
row.sort()
column.sort()
googanC = []
googanR = []

for i in range(0, len(column)-1):
    googanC.append((column[i+1] - column[i]))
    
for j in range(0, len(row)-1):
    googanR.append((row[j+1] - row[j]))
    
print(max(googanC) * max(googanR))