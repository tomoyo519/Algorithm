import sys
input = sys.stdin.readline

input_length = int(input());
words = input()
middle_num = [];
sum = 0;
for char in words:
    if( char.isdigit() ): 
        middle_num.append(char);
    else:
       
        if(len(middle_num)==0): continue;
        else:
            middle_num = ''.join(middle_num)
            sum+= int(middle_num)
            middle_num = [];
            
print(sum)
        