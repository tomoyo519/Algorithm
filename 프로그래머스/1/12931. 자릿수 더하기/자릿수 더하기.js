function solution(n)
{
    let answer  = 0;
   let arr = n.toString().split('')
   for(let i=0; i<arr.length; i++){
       if(Number(arr[i]) ===NaN) continue;
       else{
           answer+=Number(arr[i])
       }
   }
   return answer
}