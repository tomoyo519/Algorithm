function solution(arr)
{
    let answer = [];
    for(let i=0; i<arr.length; i++){
        if(answer[answer.length-1] === arr[i]){
            continue;
        }else{
            answer.push(arr[i])
        }
    }
return answer
}