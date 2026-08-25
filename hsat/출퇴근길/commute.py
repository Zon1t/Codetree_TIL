from collections import deque

N, M = map(int, input().split())

data1 = [[] for _ in range(N+1)]
data2 = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    data1[s].append(e)
    data2[e].append(s)

start, end = map(int, input().split())

visited = [0] * (N+1)
first_set = set()
Q = deque([(start, 1), (end, 2)])
while Q:
    node, bit = Q.popleft()

    for next_node in (data1[node] if bit == 1 else data2[node]):
        if visited[next_node]&bit:
            if next_node not in first_set and bit==1 and next_node not in [start, end]:
                first_set.add(next_node)
            continue

        if bit == 1 and next_node == end:
            continue

        visited[next_node] |= bit
        Q.append((next_node, bit))

for node in range(1, N+1):
    if visited[node] == 3:
        first_set.add(node)

start, end = end, start

visited = [0] * (N+1)
second_set = set()
Q = deque([(start, 1), (end, 2)])
while Q:
    node, bit = Q.popleft()

    for next_node in (data1[node] if bit == 1 else data2[node]):
        if visited[next_node]&bit:
            if next_node not in second_set and bit==1 and next_node not in [start, end]:
                second_set.add(next_node)
            continue

        if bit == 1 and next_node == end:
            continue

        visited[next_node] |= bit
        Q.append((next_node, bit))

second_set = set()
for node in range(1, N+1):
    if visited[node] == 3:
        second_set.add(node)

print(len(first_set.intersection(second_set)))