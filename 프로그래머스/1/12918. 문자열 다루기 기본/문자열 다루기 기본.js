function solution(s) {
    
    let digits = s.split('')
    let len = s.length;
    if(len ===4 || len ===6) {
        
  
    for(let i=0; i<digits.length; i++){
        if(!Number.isInteger(Number(digits[i])) ){
            return false;
            
        }
    }
          }else{
              return false
          }
    return true;
}