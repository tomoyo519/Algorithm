function solution(n, lost, reserve) {
    // 여벌의 체육복을 가져온 학생이 체육복을 도난당했을 경우
    let newLost = lost.sort().filter(l => !reserve.includes(l)) // 도난당했지만 여벌이 없는 학생
    let newReserve = reserve.sort().filter(r => !lost.includes(r)); // 여벌이 있지만 도난당하지 않은 학생

   
  
    // 여벌 체육복이 있는 학생만 빌려줄 수 있음
    for(let i=0; i<newReserve.length; i++){
        //앞번호 학생에게 빌려줄 수 있는 경우
        let reserveBody = newReserve[i]
        if(newLost.includes(reserveBody -1)){
            newLost = newLost.filter(l=> l!== (reserveBody-1))
        }else if(newLost.includes(reserveBody+1)){
            newLost = newLost.filter(l=> l!==(reserveBody +1))
        }
    }
    return n - newLost.length;
}