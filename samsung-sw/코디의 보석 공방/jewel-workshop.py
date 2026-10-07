# 개수 전역으로 관리. 판매되는 경우에 한하여 remove_set에 추가하기.
#

# 1. 보석 준비
#       - 무게와 가치에 대한 생각.
#       - 두 가지 상태에 대해서 관리해야 함.

# 2. 보석 입고
#       - 얘는 걍 append 해주면 될 듯?

# 3. 보석 판매
#       - remove set에 추가

# 4. 진열
#       - dp하면 될 듯? 텀이 너무 크긴 하다. set 활용하면 해결 가능할 듯?

# 5. 세트 구성
#       - 가장 많이 호출되는 함수이니 만큼 적절하게 투포인터 활용해서 하면 될 듯?
#       - 아마 무게로 정렬된 데이터가 필요한 듯. 무게 기준으로 검색하고 싶음.


# 결론 : bisect 활용하면 좋을 듯. 무게로 정렬된 데이터가 가장 기본이 되게끔 하고, idx 검색하면
# 가치와 무게를 알 수 있게끔 dict 활용? 아예 idx랑 같이 저장하는 것도 방법인데, 이건 고민해보자.
# 같이 저장하고 lazy하게 처리하는 편이 좋아 보인다.

from bisect import bisect_left, bisect_right, insort_left
INF = float('inf')


def init(lst):
    global stone_num, stone_cnt
    stone_num = stone_cnt = lst[0]
    for i in range(1, stone_num+1):
        w, v = lst[i*2-1], lst[i*2]
        stone.append((w, v, i))
        stone_info[i] = (w, v)
    stone.sort()


def buy(w, v):
    global stone_num, stone_cnt
    stone_num += 1
    stone_cnt += 1
    insort_left(stone, (w, v, stone_num))
    stone_info[stone_num] = (w, v)


def sell(idx):
    global stone_cnt

    if idx not in stone_info:
        return -1
    else:
        w, v = stone_info.pop(idx)
        idx = bisect_left(stone, (w, v, 0))
        stone.pop(idx)
        stone_cnt -= 1
        return v


def arrange(W):
    dp = [-1] * (W+1)
    dp[0] = 0
    for w, v in stone_info.values():
        for weight in range(W-w, -1, -1):
            if dp[weight] != -1:
                dp[weight+w] = max(dp[weight+w], dp[weight]+v)
    return max(dp)

# 더 최적화할 수 있는데 일단 제출?
def make_set(D):
    total_cnt = 0
    right = 0

    for left in range(stone_cnt):
        if right < left + 1:
            right = left + 1

        while right < stone_cnt and stone[right][0] - stone[left][0] <= D:
            right += 1

        total_cnt += right - left - 1

    return total_cnt


# ============================================================================
# 세팅

stone = []
stone_num = 0
stone_cnt = 0
stone_info = dict()
answer = []

# ============================================================================
# 실행부

for _ in range(int(input())):
    command, *data = map(int, input().split())
    if command == 1:
        init(data)
    if command == 2:
        buy(*data)
    if command == 3:
        answer.append(str(sell(data[0])))
    if command == 4:
        answer.append(str(arrange(data[0])))
    if command == 5:
        answer.append(str(make_set(data[0])))

# 정답 출력
print('\n'.join(answer))
