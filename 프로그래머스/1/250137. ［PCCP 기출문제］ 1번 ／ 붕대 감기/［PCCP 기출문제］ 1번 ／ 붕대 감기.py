def solution(bandage, health, attacks):
    # // while 문 안에서 현재체력, 연속 성공을 세야겠네
    
    completeT = bandage[0]
    healP = bandage[1]
    addP = bandage[2]
    currentH = health;
    attackT = attacks[-1][0];
    attackTime = 0;
    continousC = 0;
    for i in range(1, attackT +1):
        print('i:',i)
        print('attackTime: ',attackTime)
        print('continours:', continousC)
        if attackTime < len(attacks) and i != attacks[attackTime][0]:
            print(currentH, continousC, attacks[attackTime][0], attacks[attackTime][1])
            print('completeT', completeT)
            continousC+=1
            if continousC != completeT:
                
                currentH += healP
                if currentH > health:
                    currentH = health;
                print('after heal', currentH)
            else:  
                print('여기')
                currentH += ( healP + addP )
                continousC = 0;
                if currentH > health:
                    currentH = health;
            
        elif attackTime < len(attacks) and i == attacks[attackTime][0]:
            print(currentH, continousC, attacks[attackTime][0], attacks[attackTime][1])
            continousC = 0;
            currentH -= attacks[attackTime][1]
            attackTime+=1;
            if attackTime == len(attacks):
                attackTime = len(attacks) -1
        
            if currentH <= 0 :
                return -1
            
        


            
    return currentH