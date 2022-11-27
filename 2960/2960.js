const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split(" ");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  const num = input[0] * 1;
  let target = input[1] * 1;
  const arr = [];
  for (let i = 2; i <= num; i++) arr.push(i);
  while (target > 0) {
    let minNum = arr[0];
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] % minNum === 0) {
        result = arr[i];
        arr.splice(i, 1);
        target -= 1;
        if (target === 0) return console.log(result);
      }
    }
  }
}
