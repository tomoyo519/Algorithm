function solution(numbers) {
    let answer = []
    for(let i=0; i<numbers.length; i++){
        for(let j=1; j<numbers.length; j++){
            if(i !==j){
                let newNum = numbers[i]+numbers[j]
                answer.push(newNum)
            }
        }
    }
    let sorted = [...new Set(answer)] 
    return sorted.sort((a,b)=>a-b);
}