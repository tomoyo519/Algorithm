function solution(x) {
    
    let arr = x.toString().split('')
    let zari = arr.reduce((acc,cur)=>Number(acc)+ Number(cur))
    return x % zari === 0 ? true : false
    
}