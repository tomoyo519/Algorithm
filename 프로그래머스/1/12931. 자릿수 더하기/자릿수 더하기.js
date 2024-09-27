function solution(n)
{
   let arr = n.toString().split('')
   let answer = arr.reduce((acc,cur)=>Number(acc)  +Number(cur) , 0)
   return answer
}