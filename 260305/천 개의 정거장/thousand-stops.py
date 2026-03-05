import sys; MAX_VALUE = sys.maxsize; input = sys.stdin.readline
import heapq

A, B, N = map(int, input().split())
data_dict = dict()

for _ in range(N):
    cost, M = map(int, input().split())
    stations = list(map(int, input().split()))
    for i in range(M-1):
        for j in range(i+1, M):
            start, end = stations[i], stations[j]
            if data_dict.get((start, end)):
                if data_dict[(start, end)][0] > cost:
                    data_dict[(start, end)] = [cost, j-i]
                elif data_dict[(start, end)] == cost:
                    data_dict[(start, end)][1] = min(j-i, data_dict[(start, end)][1])
            else:
                data_dict[(start, end)] = [cost, j-i]

costs = [MAX_VALUE] * (1001)
times = [MAX_VALUE] * (1001)
visited = [False] * (1001)
costs[A] = 0
times[A] = 0

for i in range(1, 1001):
    min_idx = -1
    for j in range(1, 1001):
        if visited[j]:
            continue
        if min_idx == -1 or costs[min_idx] > costs[j]:
            min_idx = j
    visited[min_idx] = True
    for j in range(1, 1001):
        if data_dict.get((min_idx, j)) is None:
            continue
        delta_cost, delta_time = data_dict.get((min_idx, j))
        next_cost = costs[min_idx] + delta_cost
        if next_cost < costs[j]:
            costs[j] = next_cost
            times[j] = times[min_idx] + delta_time
        elif next_cost == costs[j]:
            times[j] = min(times[min_idx] + delta_time, times[j])
print(costs[B] if costs[B] != MAX_VALUE else -1, times[B] if times[B] != MAX_VALUE else -1)