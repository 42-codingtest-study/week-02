const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  let num = input[0];
  input.splice(0, 1); // input의 문자열들만 저장
  const result = [];
  for (let i = 0; i < input[0].length; i++) {
    //문자열들의 길이가 같다 해서 그냥 첫 문자의 길이로 계산
    let char = input[0][i]; // 기준이 될 문자
    for (let j = 1; j < num; j++) {
      if (input[j][i] !== char) char = "?"; // 기준 문자와 한번이라도 다르면 추가할 문자를 ? 로 변경
    }
    result.push(char);
  }
  console.log(result.join(""));
}
