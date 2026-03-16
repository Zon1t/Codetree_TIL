import sys; MAX_VALUE = sys.maxsize

N, M = map(int, input().split())
data = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    data[s][e] = d
    data[e][s] = d

def dijkstra(start):
    visited = [False] * (N+1)
    distances = [MAX_VALUE] * (N+1)
    distances[start] = 0
    for i in range(1, 1+N):
        min_idx = -1
        for j in range(1, 1+N):
            if visited[j]:
                continue
            if min_idx == -1 or distances[j] < distances[min_idx]:
                min_idx = j
        visited[min_idx] = True
        for j in range(1, 1+N):
            if data[min_idx][j] == 0:
                continue
            next_dist = data[min_idx][j] + distances[min_idx]
            if next_dist < distances[j]:
                distances[j] = next_dist
    return distances
original_distances = dijkstra(1)

track = []
def backtrack(now_node, temp_list):
    if now_node == 1:
        track.append(temp_list[::-1])
        return
    for prev_node in range(1, N+1):
        if data[now_node][prev_node] == 0:
            continue
        if original_distances[prev_node] + data[prev_node][now_node] == original_distances[now_node]:
            temp_list.append(prev_node)
            backtrack(prev_node, temp_list)
            temp_list.pop()

backtrack(N, [N])

if len(track) >= 2:
    print(0)
else:
    track = track[0]
    length = len(track) - 1
    answer = original_distances[N]
    for i in range(length):
        data[track[i]][track[i+1]] *= 2
        data[track[i+1]][track[i]] *= 2
        answer = max(answer, dijkstra(1)[N])
        data[track[i]][track[i+1]] //= 2
        data[track[i+1]][track[i]] //= 2
    print(answer - original_distances[N])