function solution(n)
{
    let answer = 0;
    let arr = n.toString().split('')
    let len = arr.length
    for(let i=0; i<len; i++){
        
        answer += Number(arr[i])
    }
    return answer;
}