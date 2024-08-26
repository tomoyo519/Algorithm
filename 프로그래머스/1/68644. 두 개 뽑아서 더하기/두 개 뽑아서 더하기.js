function solution(numbers) {
    let answer = [];
    for(let i=0 ; i<numbers.length; i++){
        for(let j=0 ; j<numbers.length; j++){
          
            let digit = numbers[i]+ numbers[j]
            if(i !== j && !answer.includes(digit)){
                answer.push(digit)
            }
        }
    }
    return answer.sort((a,b) => a - b)
}