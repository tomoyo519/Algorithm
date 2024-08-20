function solution(s) {
  let num_words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  let res = s;
  for (let i = 0; i < num_words.length; i++) {
    if (Number(res)) break;  // 영단어로 바뀐 부분이 없다면 break

    if (res.match(num_words[i])) {
      res = res.replaceAll(num_words[i], i);
    }
  }

  return Number(res);
}