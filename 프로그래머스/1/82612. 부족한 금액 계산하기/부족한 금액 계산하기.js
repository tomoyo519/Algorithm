function solution(price, money, count) {
  let sum = 0;
  for (let i = 0; i < count; i++) {
    sum += (i + 1) * price;
  }
  if (money >= sum) {
    return 0;
  }
  const diff = Math.abs(money - sum);

  return diff;
}