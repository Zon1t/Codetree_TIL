from itertools import combinations

def calc_diff(A):
    # A에 없는 원소들 받기.
    B = [i for i in range(N) if i not in A]

    # 점수 연산.
    score_A, score_B = 0, 0
    for i in range(1, N//2):
        for j in range(i):
            score_A += grid[A[j]][A[i]]
            score_B += grid[B[j]][B[i]]

    # 차이 반환
    return abs(score_A-score_B)

# 입력받기.
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 덧셈 연산이 많이 중복되므로 미리 연산해두기.
for row in range(N-1):
    for col in range(row, N):
        grid[row][col] += grid[col][row]

# N//2개만큼 뽑으며 점수 연산. 이때 0은 A그룹에 고정하고 나눔.
answer = float('inf')
for t_ in combinations(range(1, N), N//2-1):
    temp = calc_diff((0,) + t_)
    if temp < answer:
        answer = temp

print(answer)