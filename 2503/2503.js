const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  let arr = [];
  for (let i = 1; i < 10; i++) {
    for (let j = 1; j < 10; j++) {
      if (j === i) continue;
      for (let k = 1; k < 10; k++) {
        if (k === j || k === i) continue;
        arr.push("" + i + j + k);
      }
    }
  }
  //   console.log(arr);
  // 중복되지않는 3자리 숫자들 배열 생성

  let n = input[0] * 1;
  for (let i = 1; i <= n; i++) {
    const minhyeokInput = input[i].split(" ")[0];
    const sc = input[i].split(" ")[1] * 1;
    const bc = input[i].split(" ")[2] * 1;
    const answer_arr = [];
    let s, b;

    arr.forEach((num) => {
      s = 0;
      b = 0;
      for (let x = 0; x < 3; x++) {
        for (let y = 0; y < 3; y++) {
          if (x === y && minhyeokInput[x] === num[y]) s++;
          if (x !== y && minhyeokInput[x] === num[y]) b++;
        }
      }
      if (s === sc && b === bc) {
        answer_arr.push(num);
      }
    });
    arr = answer_arr;
  }
  console.log(arr.length);
}
