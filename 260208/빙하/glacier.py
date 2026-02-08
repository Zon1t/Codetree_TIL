n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

# def find_hole():
#     hole_list = []
#     for row in range(1, n-1):
#         for col in range(1, m-1):
#             if grid[row][col] == 0 and check_escape(row, col):
#                 hole_list.append((row, col))
#     return hole_list

# # 이 부분 dfs로 세팅하면 시간복잡도가 줄어들 것으로 예상? -> 이따 수정해보기

# def check_escape(row, col):
#     visited = [[False]*m for _ in range(n)]
#     q = deque([(row, col)])
#     visited[row][col] = True
#     while q:
#         r, c = q.popleft()
#         for i in range(4):
#             nr, nc = r + dr[i], c + dc[i]
#             if 0 <= nr < n and 0 <= nc < m:
#                 if not visited[nr][nc] and grid[nr][nc] == 0:
#                     q.append((nr, nc))
#                     visited[nr][nc] = True
#             else:
#                 return False
#     return True


# 빙하 다 append -> 근처에 0 있으면 q에 append. but hole_list 안에 존재하면 pass
# q에 있는 애들 다 0으로 값 변경.걔네들 기준으로 근처에 있는 1값 append.
# 반복. -> 이렇게 했을 때 hole이 더 이상 아니게 된 경우에 문제가 발생한다.
# 매턴 find_hole 함수 적용..?

# 매턴 find_hole 함수 적용시 : while문으로 턴 및 마지막 남은 빙하 수 계산
# 시간 초과 문제. -> 사라진 애들을 기준으로 append하기???
# -> hole에 대한 처리 문제 발생

# 아예 처음부터 외부에서 bfs돌기 -> 1 만나면 체크하고 녹이기 반복.
# 이게 더 시간복잡도 상으로 이득인가? 그런 것 같다.

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

s = 0
count_list = [0]
while True:
    q = deque([(0, 0)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    count = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if grid[nr][nc]:
                    visited[nr][nc] = True
                    grid[nr][nc] = 0
                    count += 1
                else:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    if count:
        count_list.append(count)
        s += 1
    else:
        break
print(s, count_list[-1])