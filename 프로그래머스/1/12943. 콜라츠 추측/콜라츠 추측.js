function solution(num) {
    let count = 0;
    let numCpy = num;
    while(numCpy !==1 ){
        if(count >=500){
            return -1;
            break;
            
        }
        if(numCpy % 2 === 0){
            numCpy /=2
            count++
        }
        else if(numCpy % 2 ===1){
            numCpy = numCpy * 3 +1
            count++
        }
    }
    
    return count >=500 ? -1 : num ===1 ? 0 : count
}