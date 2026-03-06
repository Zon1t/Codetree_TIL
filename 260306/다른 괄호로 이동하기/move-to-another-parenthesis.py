import sys; MAX_VALUE = sys.maxsize; input = sys.stdin.readline
import heapq

N, A, B = map(int, input().split())
total_num = N**2
grid = [input().strip() for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return (0 <= row < N and 0 <= col < N)

def dijkstra(row, col):
    costs = [[MAX_VALUE]*N for _ in range(N)]
    costs[row][col] = 0
    Q = [(0, row, col)]
    while Q:
        curr_cost, curr_row, curr_col = heapq.heappop(Q)
        curr_value = grid[curr_row][curr_col]
        if curr_cost > costs[curr_row][curr_col]:
            continue
        for i in range(4):
            next_row, next_col = curr_row + dr[i], curr_col + dc[i]
            if not in_range(next_row, next_col):
                continue
            next_value = grid[next_row][next_col]
            cost = A if curr_value == next_value else B
            next_cost = curr_cost + cost
            if next_cost < costs[next_row][next_col]:
                costs[next_row][next_col] = next_cost
                heapq.heappush(Q, (next_cost, next_row, next_col))
    return max([max(row) for row in costs])

answer = 0
for row in range(N):
    for col in range(N):
        now_max = dijkstra(row, col)
        answer = now_max if answer < now_max else answer

print(answer)