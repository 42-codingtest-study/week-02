from itertools import permutations

### 🙇🏻‍♀️ 솔 직 고 백 🙇🏻‍♀️
### 많은 시도 끝에 블로그를 참고하였고 그래서 주석을 자세히 작성합니다 ...
### permutations 함수를 사용할 생각을 어떻게 하는 건지 모르겠어요 ...
### 모든 조합을 다 확인하면 시간 초과가 날 것만 같은데 아니네요 ? 신기해요
### 🖤🖤🖤🖤🖤🖤🖤🖤🖤

# 1부터 9까지 서로 다른 수의 세 자리 숫자 조합
nums = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))

n = int(input())

for _ in range(n):
    question, strike, ball = map(int, input().split())
    # 민혁이가 영수에게 제시한 세 자리 수
    question = list(str(question))

    # nums의 길이가 변함에 따라 인덱스를 조정해주기 위한 변수
    removed = 0

    # 모든 조합을 확인
    for i in range(len(nums)):
        cnt_s, cnt_b = 0, 0

        # ex) 이전에 i번째 항목이 지워졌다면 다시 i번째 항목을 봐야함
        #     안지워졌다면 그냥 i + 1번째 항목을 보면 됨
        i -= removed

        # 민혁이가 제시한 3자리 수를 한 개씩 확인
        for j in range(3):
            # 동일한 자리에 위치하면 스트라이크 카운트 증가
            if int(question[j]) == nums[i][j]:
                cnt_s += 1
            # 있긴 하나 다른 자리에 위치하면 볼 카운트 증가
            elif int(question[j]) in nums[i]:
                cnt_b += 1

        # 영수가 대답한 조건과 다르면 그 조합은 배열에서 지워줌
        if not(strike == cnt_s and ball == cnt_b):
            nums.remove(nums[i])
            removed += 1

# nums는 영수의 생각하고 있는 세 자리 수 조건에 맞는 조합만 남은 상태
print(len(nums))