def factorial(n):
    if(n == 0 or n==1):
        return 1;
    else:
        return int(n) * factorial(n-1)
        
number = int(input());

print(factorial(number))
