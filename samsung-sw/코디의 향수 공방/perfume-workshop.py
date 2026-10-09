# []/
# 1. 향료 준비
#       - idx, degree 값을 적절하게 저장하면 될 듯.
#       - 아래 작업들 보고 어떻게 저장할지 체크해야 할 듯

# 2. 향료 추자
#       - 폐기된 번호 재사용X -> 전역으로 cnt 확인해가며 추가해가자.

# 3. 향료 폐기
#       - dict로 관리하기

# 4. 블렌딩
#       - 전형적인 dp 문제 형식이다. dp 테이블 만들고 ㄱㄱ

# 5. 향수 구성
#       - 3개면 음.. 두개 만들고 찾는 느낌으로 가면 될 것 같은데..?
#       - 자리가 구분된다는 사실이 중요한 것 같다. 걍 하면 될 듯?


# 향도 기준으로 정렬된 자료가 필요하다. idx 검색으로 향도를 뽑을 수 있게 하고 bisect 활용해서
# 제거할 수 있게끔? 추가할 수 있게끔? 하면 될 것으로 판단된다.

from bisect import bisect_left, insort_left


def init():
    for i in range(1, N+1):
        perfume_lst.append(init_data[i+1])
        search[i] = init_data[i+1]
    perfume_lst.sort()


def add(v):
    global cnt, N
    cnt += 1
    N += 1

    insort_left(perfume_lst, v)
    search[cnt] = v


def remove(idx):
    global N
    if idx not in search:
        return -1

    N -= 1
    pos = bisect_left(perfume_lst, search[idx])
    perfume_lst.pop(pos)
    return search.pop(idx)


def blending(k):
    dp = [INF] * (k+1)
    dp[0] = 0

    for v in perfume_lst:
        for w in range(k-v+1):
            if dp[w] != INF:
                dp[w+v] = min(dp[w+v], dp[w]+1)

    return -1 if dp[k] == INF else dp[k]


def compose(k):
    total_cnt = 0
    for first_v in perfume_lst:
        for second_v in perfume_lst:
            now_sum = first_v + second_v
            pos = bisect_left(perfume_lst, k-now_sum)
            total_cnt += N-pos
    return total_cnt


# ====================================================================
# 세팅

search = dict()
perfume_lst = []

Q = int(input())
init_data = list(map(int, input().split()))
commands = [map(int, input().split()) for _ in range(Q-1)]

cnt = N = init_data[1]
answer = []

INF = float('inf')
init()

# ====================================================================
# 실행부

for command, data in commands:
    if command == 2: add(data)
    elif command == 3: answer.append(str(remove(data)))
    elif command == 4: answer.append(str(blending(data)))
    else: answer.append(str(compose(data)))

print('\n'.join(answer))