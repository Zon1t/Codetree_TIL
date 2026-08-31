def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def cal(arr):
    # sort 해서 위의 꼭지점, 아래 꼭지점 세기만 세면 안될거같은데

    # 제일 r이 작은거 제일 c가 작은거
    start_r  = int(1e9)
    start_c = 0
    end_r = int(-1e9)
    end_c = 0

    left_c =  int(1e9)
    left_r = 0
    right_c = int(-1e9)
    right_r = 0

    for r,c in arr:
        if start_r > r:
            start_r = r
            start_c = c
        if end_r < r:
            end_r = r
            end_c = c


        if left_c > c:
            left_r = r
            left_c = c

        if right_c < c:
            right_c = c
            right_r = r

    visited = [[0] * N for _ in range(N)]

    # 1번 부족 경계값 체크하기
    for (r,c) in arr:
        visited[r][c] = 1 # 다 표시해놓기

    sum_people = [0] * 6

    for i in range(start_r):
        for j in range(start_c+1):
            sum_people[2] += people[i][j]
        for j in range(start_c+1, N):
            sum_people[3] += people[i][j]

    # 끝 지점이라면
    for i in range(end_r+1, N):
        for j in range(end_c):
            sum_people[4] += people[i][j]
        for j in range(end_c, N):
            sum_people[5] += people[i][j]

    for i in range(start_r, end_r+1):
        target = 0
        is_check = False
        is_five = False
        # 왼쪽이 더 큰 경우
        if left_r > right_r:
            # 그러면 구간은 sr ~ rr , rr~ lr ,lr~er 이다.
            if start_r <= i <= right_r:
                target = 2
            elif right_r <= i <= left_r:
                target = 4
                is_five = True # 5로 늘릴 예정

            elif left_r <= i <= end_r:
                target = 4

        elif right_r > left_r:
            if start_r <= i < left_r:
                target = 2
            elif left_r<= i <= right_r:
                target = 4
                is_check = True # 3으로 줄여야 한다.
            elif right_r <= i <= end_r:
                target = 4

        elif right_r == left_r:
            if start_r <= i < left_r:
                target = 2
            elif i == right_r:
                is_check = True
                target = 4
            elif right_r <= i <= end_r:
                target = 4

        is_one = False
        is_pass = False
        need_skip = False
        for j in range(N):
            if need_skip:
                need_skip = False
                if visited[i][j] == 0:
                    if is_one:
                        if is_five:
                            sum_people[target+1] += people[i][j]
                        elif is_check:
                            sum_people[target-1] += people[i][j]
                        else:
                            sum_people[target+1] += people[i][j]
                    else:
                        sum_people[target] += people[i][j]
                elif visited[i][j] == 1:
                    is_one = True
                    is_pass = True
                continue
            if is_pass:
                if i == start_r or i == end_r:
                    is_pass = False
                elif visited[i][j] == 1:
                    is_pass = False
                    need_skip = True
                    continue
                else: # 0일 때는 그냥 넘기고 옮기기
                    continue

            # visited가 1 나오기 전까지 2로 채우고 1 나오면 3으로 채우기
            if visited[i][j] == 0:
                if is_one:
                    if is_five:
                        sum_people[target+1] += people[i][j]
                    elif is_check:
                        sum_people[target-1] += people[i][j]
                    else:
                        sum_people[target+1] += people[i][j]
                else:
                    sum_people[target] += people[i][j]
            elif visited[i][j] == 1:
                is_one = True
                is_pass = True

    sum_people[1] = total - sum(sum_people[2:])
    return (max(sum_people[1:]) - min(sum_people[1:]))

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

N = int(input())

people = [] # 각 위치의 사람 수 배열
for _ in range(N):
    people.append(list(map(int,input().split())))

total = sum([sum(row) for row in people])
answer = 40000
for sr in range(2, N):
    for sc in range(1, N-1):
        for first_step in range(1, N):
            for second_step in range(1, N-first_step+1):
                standard_point = [(sr, sc)]
                curr_row, curr_col = sr, sc

                # 끝단 꼭짓점 연산하기.
                keep = True
                for d in range(4):
                    for k in range(1, (first_step if d%2 == 0 else second_step)+1):
                        curr_row, curr_col = curr_row + dr[d], curr_col + dc[d]
                        if not in_range(curr_row, curr_col):
                            keep = False
                            break
                        standard_point.append((curr_row, curr_col))
                    if not keep:
                        break
                if not keep:
                    continue

                # 나머지 부족 사람 수 연산하러 ㄱㄱㅆ
                temp = cal(standard_point)
                if answer > temp:
                    answer = temp

# 정답 출력
print(answer)