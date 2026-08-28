# 전체 양분을 관리해야 하므로 grid를 직접 그리는 방법 채택
# 바이러스는 따로 dictionary로 관리해도 될 것 같다.

# 시간초과 발생; 너무 대충 관리했나 싶기도 하다. 줄일 수 있는 부분이 있을까?
# 힙쓰지 말기 -> 귀찮아도 걍 필요할 때 sort해주자.

import heapq

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def eat():
    # 양분을 섭취하는 로직.
    for row, col in list(virus_dict.keys()):
        new_lst = []
        yangboon = 0
        virus_dict[(row, col)].sort()
        for age in virus_dict[(row, col)]: # 정렬해서 괜찮을 듯?
            if age > yangboon_grid[row][col]:
                yangboon += age>>1
            else:
                yangboon_grid[row][col] -= age
                new_lst.append(age+1)
                if (age+1)%5 == 0:
                    age_5.append((row, col))
        yangboon_grid[row][col] += yangboon

        if new_lst:
            virus_dict[(row, col)] = new_lst
        else:
            virus_dict.pop((row, col))

def burnsick():
    # 번식시키기
    for row, col in age_5:
        for d in range(8):
            next_row, next_col = row + dr[d], col + dc[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if (next_row, next_col) in virus_dict:
                virus_dict[(next_row, next_col)].append(1)
            else:
                virus_dict[(next_row, next_col)] = [1]
    # 다 번식했으면 비우기
    age_5.clear()

def update():
    for row in range(N):
        for col in range(N):
            yangboon_grid[row][col] += update_grid[row][col]

def count_virus():
    answer = 0
    for _, lst in virus_dict.items():
        answer += len(lst)
    return answer

def custom_print():
    print(t)
    print(virus_dict)
    for row in yangboon_grid:
        print(*row)


N, K, T = map(int, input().split())
update_grid = [list(map(int, input().split())) for _ in range(N)]

yangboon_grid = [[5]*N for _ in range(N)]
virus_dict = dict()
for _ in range(K):
    row, col, age = map(int, input().split())
    row, col = row-1, col-1

    if (row, col) in virus_dict:
        virus_dict[(row, col)].append(age)
    else:
        virus_dict[(row, col)] = [age]

# 5의 배수 나이를 가진 바이러스를 업데이트하기 위함.
age_5 = []
for t in range(T):
    # 1. 양분 먹기 및 바이러스 정리
    eat()

    # 2. 번식 진행
    burnsick()

    # 3. 양분 양 업데이트 하기
    update()

# 4. 정답 연산 후 출력
answer = count_virus()
print(answer)