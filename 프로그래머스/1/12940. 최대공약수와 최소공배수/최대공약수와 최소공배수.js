function solution(n, m) {
    let min = 0
    let max = 0
    if (n > m)  {
        min = m
        max = n
    }else{
        min = n
        max = m
    }
    let max_yaksu = [];
    let min_baesu = [];
    for(let i=1; i<=max; i++){
        if(n % i ===0 && m % i === 0){
            max_yaksu.push(i)
            
        }
        // 최소공배수 어케 구하지
        
    }
    for(let j=1; j<=min; j++){
        min_baesu.push(j*max)
    }
    const result = min_baesu.filter((baesu) => baesu%min === 0)
    return [Math.max(...max_yaksu), Math.min(...result)];
}