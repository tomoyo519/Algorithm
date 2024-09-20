function solution(arr) {
    if (arr.length === 0) return [];  

    const result = [];  
    let lastNum = null; 

    for (let num of arr) {
        if (num !== lastNum) { 
            result.push(num);  
            lastNum = num;    
        }
    }

    return result;
}
