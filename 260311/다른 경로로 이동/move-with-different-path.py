import sys; MAX_VALUE = sys.maxsize

N, M = map(int, input().split())
data = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    data[s][e] = d
    data[e][s] = d

def dijkstra(start):
    distances[start] = 0
    for i in range(1, N+1):
        min_idx = -1
        for j in range(1, N+1):
            if visited[j]:
                continue
            if min_idx == -1 or distances[j] < distances[min_idx]:
                min_idx = j
        visited[min_idx] = True
        for j in range(1, N+1):
            if data[min_idx][j] == 0:
                continue
            next_dist = distances[min_idx] + data[min_idx][j]
            if next_dist < distances[j]:
                distances[j] = next_dist

distances = [MAX_VALUE] * (N+1)
visited = [False] * (N+1)
dijkstra(1)

track = []
def backtrack(now_node, now_distance, temp_list):
    if now_node == 1:
        track.append(temp_list[::-1])
        return
    for j in range(1, N+1):
        if data[now_node][j] == 0:
            continue
        if now_distance - data[now_node][j] == distances[j]:
            temp_list.append(j)
            backtrack(j, now_distance - data[now_node][j], temp_list)
            temp_list.pop()
backtrack(N, distances[N], [N])
track.sort()
real_track = track[0]
for i in range(len(real_track)-1):
    data[real_track[i]][real_track[i+1]] = 0
    data[real_track[i+1]][real_track[i]] = 0

distances = [MAX_VALUE] * (N+1)
visited = [False] * (N+1)
dijkstra(1)
print(distances[N] if distances[N] != MAX_VALUE else -1)