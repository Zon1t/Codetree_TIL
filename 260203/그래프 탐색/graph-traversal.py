n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visited = [False] * (n+1)
visited[1] = True
num_dict = dict()
for A, B in edges:
    if num_dict.get(A):
        num_dict[A].append(B)
    else:
        num_dict[A] = [B]
    if num_dict.get(B):
        num_dict[B].append(A)
    else:
        num_dict[B] = [A]

from collections import deque

q = deque([1])
while q:
    num = q.popleft()
    for temp in num_dict.get(num, []):
        if not visited[temp]:
            q.append(temp)
            visited[temp] = True

print(sum(visited)-1)