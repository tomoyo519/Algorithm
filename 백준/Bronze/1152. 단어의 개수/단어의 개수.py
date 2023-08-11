number = 0;
sentence = list(str(input()))
if(sentence[0] ==' ' and sentence[-1] == ' '):
    sentence = sentence[1:len(sentence)-1]
elif(sentence[0]== ' '):
    sentence = sentence[1:]
elif(sentence[-1] == ' '):
    sentence= sentence[:len(sentence)-1]

for i in sentence:
    if(i == ' '):
        number += 1;
        
if(len(sentence) == 0):
    print(0)
else:
    print(number + 1)