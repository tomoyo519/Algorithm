def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    numA=numB=numC = 0
    for i , j in enumerate(answers):
        if i >= 5: 
            i = i % 5;
        if j == a[i]:
            numA+=1    
    for i , j in enumerate(answers):
        if i >= 8: 
            i = i % 8;
        if j == b[i]:
            numB+=1 
    for i , j in enumerate(answers):
        if i >= 10: 
            i = i % 10;
        if j == c[i]:
            numC+=1 
    result = [numA, numB, numC]
    maxResult = max(result)
    data= []
    print(result)
    for i in range(len(result)):
        if result[i] == maxResult:
            data.append(i+1)
            
    return data
            
            