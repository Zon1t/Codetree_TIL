import heapq
INF = float('inf')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

delta_grid = {1: [None, None, 5, 14, 30, 55],
              2: [None, None, None, 10, 26, 51],
              3: [None, None, None, None, 17, 42],
              4: [None, None, None, None, None, 26]}


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def dijkstra(start_row, start_col, end_row, end_col):
    dist = [[[INF] * 6 for _ in range(N)] for _ in range(N)]
    dist[start_row][start_col][1] = 0

    hq = [(0, 1, start_row, start_col)]
    while hq:
        curr_dist, curr_power, curr_row, curr_col = heapq.heappop(hq)

        if curr_row == end_row and curr_col == end_col:
            return dist[end_row][end_col][curr_power]

        if dist[curr_row][curr_col][curr_power] < curr_dist:
            continue

        for d in range(4):
            for next_power in range(1, 6):
                next_row, next_col = curr_row + dr[d] * next_power, curr_col + dc[d] * next_power

                if not in_range(next_row, next_col) or grid[next_row][next_col] == '#':
                    break
                if grid[next_row][next_col] == 'S':
                    continue

                next_dist = curr_dist + (1 if next_power == curr_power else 2 if next_power < curr_power else delta_grid[curr_power][next_power])
                if next_dist < dist[next_row][next_col][next_power]:
                    dist[next_row][next_col][next_power] = next_dist
                    heapq.heappush(hq, (next_dist, next_power, next_row, next_col))
    return -1


N = int(input())
grid = [input() for _ in range(N)]
answer = []
for _ in range(int(input())):
    start_row, start_col, end_row, end_col = map(lambda x: int(x)-1, input().split())
    answer.append(str(dijkstra(start_row, start_col, end_row, end_col)))
print('\n'.join(answer))