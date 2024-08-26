function solution(n) {
    let arr = n.toString().split('')
    let digitCount = arr.length;

    let answer = []
    for(let i=digitCount-1; i>=0; i--){
        
        answer.push(Number(arr[i]));
    }
    return answer;
}