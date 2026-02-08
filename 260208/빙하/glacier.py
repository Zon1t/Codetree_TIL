n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

def find_hole():
    hole_list = []
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 0 and check_escape(row, col):
                hole_list.append((row, col))
    return hole_list       

def check_escape(row, col):
    visited = [[False]*m for _ in range(n)]
    q = deque([(row, col)])
    visited[row][col] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True
            else:
                return False
    return True


# 빙하 다 append -> 근처에 0 있으면 q에 append. but hole_list 안에 존재하면 pass
# q에 있는 애들 다 0으로 값 변경.걔네들 기준으로 근처에 있는 1값 append.
# 반복. -> 이렇게 했을 때 hole이 더 이상 아니게 된 경우에 문제가 발생한다.
# 매턴 find_hole 함수 적용..?

# 매턴 find_hole 함수 적용시 : while문으로 턴 및 마지막 남은 빙하 수 계산

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

s = 0
count = 0
while True:
    hole_list = find_hole()
    remove_list = []
    one_list = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]
    for r, c in one_list:
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and (nr, nc) not in hole_list:
                if (r, c) not in remove_list:
                    remove_list.append((r, c))
    if remove_list:
        s += 1
        count = len(remove_list)
        for r, c in remove_list:
            grid[r][c] = 0
    else:
        break
print(s, count)