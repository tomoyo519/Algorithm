function solution(s) {
    let sArr = s.split('')
    
    let cap =[]
    let low = []
    for(let i=0; i<sArr.length; i++){
        if(sArr[i] == sArr[i].toUpperCase()){
            cap.push(sArr[i])
        }
        else low.push(sArr[i])
    }
    cap = cap.sort((a, b) => b.localeCompare(a)).join('');
    low = low.sort((a,b)=>b.localeCompare(a)).join('')
   return (low + cap)
}