import sys; MAX_VALUE = sys.maxsize; input = sys.stdin.readline
import heapq

A, B, N = map(int, input().split())
data_dict = dict()

# 메모리 초과 코드

# for _ in range(N):
#     cost, M = map(int, input().split())
#     stations = list(map(int, input().split()))
#     for i in range(M-1):
#         for j in range(i+1, M):
#             start, end = stations[i], stations[j]
#             if data_dict.get((start, end)):
#                 if data_dict[(start, end)][0] > cost:
#                     data_dict[(start, end)] = [cost, j-i]
#                 elif data_dict[(start, end)] == cost:
#                     data_dict[(start, end)][1] = min(j-i, data_dict[(start, end)][1])
#             else:
#                 data_dict[(start, end)] = [cost, j-i]

# costs = [MAX_VALUE] * (1001)
# times = [MAX_VALUE] * (1001)
# visited = [False] * (1001)
# costs[A] = 0
# times[A] = 0

# for i in range(1, 1001):
#     min_idx = -1
#     for j in range(1, 1001):
#         if visited[j]:
#             continue
#         if min_idx == -1 or costs[min_idx] > costs[j]:
#             min_idx = j
#     visited[min_idx] = True
#     for j in range(1, 1001):
#         if data_dict.get((min_idx, j)) is None:
#             continue
#         delta_cost, delta_time = data_dict.get((min_idx, j))
#         next_cost = costs[min_idx] + delta_cost
#         if next_cost < costs[j]:
#             costs[j] = next_cost
#             times[j] = times[min_idx] + delta_time
#         elif next_cost == costs[j]:
#             times[j] = min(times[min_idx] + delta_time, times[j])
# print(costs[B] if costs[B] != MAX_VALUE else -1, times[B] if times[B] != MAX_VALUE else -1)

for _ in range(N):
    cost, M = map(int, input().split())
    stations = list(map(int, input().split()))
    for i in range(M-1):
        for j in range(i+1, M):
            start, end = stations[i], stations[j]
            if data_dict.get(start):
                if data_dict[start].get(end):
                    if cost < data_dict[start][end][0]:
                        data_dict[start][end] = (cost, j-i)
                    elif cost == data_dict[start][end][1]:
                        data_dict[start][end] = (cost, min(data_dict[start][end][1], j-i))
                else:
                    data_dict[start][end] = (cost, j-i)
            else:
                data_dict[start] = {end:(cost, j-i)}

costime = [[MAX_VALUE]*2 for _ in range(1001)]
costime[A][0] = costime[A][1] = 0
Q = [(0, A)]
while Q:
    curr_cost, curr_node = heapq.heappop(Q)
    if curr_cost > costime[curr_node][0]:
        continue
    for next_node in data_dict.get(curr_node, []):
        delta_cost, delta_time = data_dict[curr_node].get(next_node, (-1, -1))
        if delta_cost == -1:
            break
        next_cost = curr_cost + delta_cost
        if next_cost < costime[next_node][0]:
            costime[next_node][0] = next_cost
            costime[next_node][1] = costime[curr_node][1] + delta_time
            heapq.heappush(Q, (next_cost, next_node))
        elif next_cost == costime[next_node][0]:
            costime[next_node][1] = min(costime[next_node][1], costime[curr_node][1] + delta_time)

print(costime[B][0] if costime[B][0] != MAX_VALUE else -1, costime[B][1] if costime[B][1] != MAX_VALUE else -1)