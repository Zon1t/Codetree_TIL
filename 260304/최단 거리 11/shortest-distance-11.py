import sys; MAX_VALUE = sys.maxsize
import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

start, end = map(int, input().split())

distance = [MAX_VALUE] * (N+1)
distance[start] = 0
Q = [(0, start)]
while Q:
    curr_dist, curr_node = heapq.heappop(Q)
    if curr_dist > distance[curr_node]:
        continue
    for next_node, weight in graph[curr_node]:
        next_dist = curr_dist + weight
        if next_dist < distance[next_node]:
            distance[next_node] = next_dist
            heapq.heappush(Q, (next_dist, next_node))

answer_list = []
def backtrack(now_node, temp_list):
    if now_node == end:
        heapq.heappush(answer_list, temp_list[:])
        return
    for next_node, diff_distance in graph[now_node]:
        if distance[next_node] - distance[now_node] == diff_distance:
            temp_list.append(next_node)
            backtrack(next_node, temp_list)
            temp_list.pop()

backtrack(start, [start])
print(distance[end])
print(*answer_list[0])