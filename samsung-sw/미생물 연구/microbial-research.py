# 미생물 연구 2차
from collections import deque

DEBUG = False
def myprint(string):
    if not DEBUG:
        return
    print(f"========{string}=========")
    for row in matrix:
        print(*row)

dxdy = [(1,0),  (0,1),(-1,0), (0,-1)]
inrange = lambda x, y : bool(0<=x<N and 0<=y < N)
def transform(r, c):
    return N-c, r


def bfs(cur_num):
    removed = set()
    coords = [set() for _ in range(cur_num+1)]
    criteria = [(-1,-1) for _ in range(cur_num + 1)]
    visited = [[0]*N for _ in range(N)]
    q = deque()

    rm_flag = False
    for x in range(N):
        for y in range(N):
            if not matrix[x][y] or visited[x][y]:
                continue
            num = matrix[x][y]
            if num in removed:
                rm_flag = True

            if coords[num]: # 두조각 됨
                rm_flag = True
                removed.add(num)
                rx, ry = criteria[num]
                for rm_x, rm_y in coords[num]:
                    nx, ny = rm_x + rx, rm_y + ry
                    matrix[nx][ny] = 0
                coords[num].clear()
            else:
                criteria[num] = (x,y) #상대좌표를 위한 시작점
            q.append((x,y))
            visited[x][y] = 1
            while q:
                cur_x, cur_y = q.popleft()

                if rm_flag:
                    matrix[cur_x][cur_y] = 0
                else:
                    rx, ry = criteria[num]
                    coords[num].add((cur_x - rx, cur_y- ry))
                for dx, dy in dxdy:
                    nx, ny = cur_x + dx, cur_y + dy
                    if not inrange(nx,ny) or visited[nx][ny]:
                        continue
                    if matrix[nx][ny] == num:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
            
            rm_flag = False

    return coords

def move(coords, cur_num):
    global  matrix
    cand = []
    for num in range(1, cur_num+1):
        if len(coords[num]) == 0:
            continue
        cand.append((- len(coords[num]), num ))

    cand.sort()
    new_ma = [[0]*N for _ in range(N)]

    alive = [0 for _ in range(cur_num + 1)]
    for _, num in cand:
        that_coord = (-1,-1)
        for s_y in range(N):
            for s_x in range(N-1, -1, -1):
                for rx, ry in coords[num]:
                    nx, ny = s_x + rx, s_y + ry
                    if not inrange(nx,ny) or new_ma[nx][ny]:
                        break
                else:
                    that_coord = (s_x, s_y)
                    break
            if that_coord != (-1,-1):
                break

        if that_coord != (-1,-1):
            s_x, s_y = that_coord
            for rx, ry in coords[num]:
                nx, ny = s_x + rx, s_y + ry
                new_ma[nx][ny] = num
            alive[num] = len(coords[num])

    matrix = new_ma
    return alive



N, Q = map(int, input().split())

matrix = [[0]*N for _ in range(N)]


for num in range(1,Q +1):
    r1, c1, r2, c2 = map(int, input().split())
    x1, y1 = transform(r1, c1)
    x2, y2 = transform(r2, c2)

    if DEBUG:
        print(f'for {num}')
        print(x1, y1)
        print(x2, y2)
    for x in range(x2, x1):
        for y in range(y1, y2):
            matrix[x][y] = num

    myprint(f"after inject {num}")

    coords  = bfs(num)
    myprint(f"after bfs ")

    alive = move(coords, num)

    myprint(f"after move ")

    answer = 0
    count_set = set()
    for x in range(N):
        for y in range(N):
            if not matrix[x][y]:
                continue
            num1 = matrix[x][y]
            for dx, dy in dxdy[:2]:
                nx,ny = x+dx, y + dy
                if not inrange(nx,ny) or not matrix[nx][ny]:
                    continue
                num2 = matrix[nx][ny]
                if num1 == num2:
                    continue
                minnum = min(num1, num2)
                maxnum = max(num1, num2)
                if (minnum, maxnum) in count_set:
                    continue
                answer += alive[num1]* alive[num2]
                count_set.add((minnum, maxnum))
    print(answer)
