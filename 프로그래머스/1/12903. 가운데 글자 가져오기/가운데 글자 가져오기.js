function solution(s) {
    let digits = s.split('')
    let len = digits.length;
    
    // qwer length === 4
    // 두글자를 반환하는 경우
    if (len % 2 === 0){
      
        let result = ''
        result =  digits[len / 2-1]+digits[len/2 ]
        return result
    }
    else{
        return digits[Math.ceil(len/2-1)]
    }
}