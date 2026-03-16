import sys; MAX_VALUE = sys.maxsize
import heapq

N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    data[s].append((d, e))
    data[e].append((d, s))

Q = [(0, N)]
distances = [MAX_VALUE] * (N + 1)
distances[N] = 0
while Q:
    curr_dist, curr_node = heapq.heappop(Q)
    if distances[curr_node] < curr_dist:
        continue
    for delta, next_node in data[curr_node]:
        next_dist = curr_dist + delta
        if next_dist < distances[next_node]:
            distances[next_node] = next_dist
            heapq.heappush(Q, (next_dist, next_node))

print(max(distances[1:]))