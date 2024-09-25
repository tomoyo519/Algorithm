function solution(s) {

   let arr = s.split('')
   console.log(arr.length)
    // 문자열의 길이가 4가 아니거나 혹은 6이 아니거나 할때 return false 하고싶음
    
    if (arr.length !== 4 && arr.length !== 6) {
    return false;
  }

    for(let i=0; i<arr.length; i++){
        console.log(Number(arr[i]))
        if(!Number.isInteger(Number(arr[i])))return false
    }
    


    
    return true
}