def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    numA=numB=numC = 0
    for i , j in enumerate(answers):
        if j == a[i%5]:
            numA+=1    
        if j == b[i%8]:
            numB+=1 
        if j == c[i%10]:
            numC+=1 
    result = [numA, numB, numC]
    data= []
    for i in range(len(result)):
        if result[i] == max(result):
            data.append(i+1)
            
    return data
            
            