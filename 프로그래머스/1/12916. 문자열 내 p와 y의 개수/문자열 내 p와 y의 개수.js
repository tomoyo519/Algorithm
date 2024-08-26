function solution(s){
    let pCount = 0;
    let yCount = 0;
    let arr = s.split('')
    for(let i=0; i<arr.length; i++){
        if(arr[i] === 'p' || arr[i] ==='P'){
            pCount ++
        }
        else if(arr[i] === 'y' || arr[i] ==='Y'){
            yCount ++
        }
    }
     return pCount === yCount ?  true :  false
    }