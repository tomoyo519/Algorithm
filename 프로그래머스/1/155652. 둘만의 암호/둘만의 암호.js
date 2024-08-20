function solution(s, skip, index) {
    const skipSet = new Set(skip); // skip 알파벳을 Set으로 저장
    let result = '';

    for (let char of s) {
        let newIndex = 0;
        let currentChar = char;

        // index만큼 뒤로 이동
        while (newIndex < index) {
            currentChar = String.fromCharCode((currentChar.charCodeAt(0) - 97 + 1) % 26 + 97); // 알파벳 이동
            if (!skipSet.has(currentChar)) {
                newIndex++;
            }
        }
        result += currentChar; // 변환된 문자 추가
    }

    return result;
}