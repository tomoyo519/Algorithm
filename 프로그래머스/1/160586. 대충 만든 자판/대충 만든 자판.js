function solution(keymap, targets) {
  const answer = [];
  const map = new Map(); // 각 키의 입력 횟수 저장

  for (const key of keymap) { // keymap 의 각 키 반복
    for (let i = 0; i < key.length; i++) {
    // 해당 키가 이미 맵에 존재하지 않거나, 현재 인덱스보다 작은 값이 저장되어있다면, 인덱스 +1 값 맵에 저장
      if (!map.has(key[i]) || i + 1 < map.get(key[i])) map.set(key[i], i + 1);
    }
  }

  for (const target of targets) {
    let count = 0;
    for (let i = 0; i < target.length; i++) {
      count += map.get(target[i]);
    }
    answer.push(count || -1); // count가 0인경우(타겟 문자열에 포함된 키가 키맵에 없는경우) -1 추가
  }

  return answer;
}