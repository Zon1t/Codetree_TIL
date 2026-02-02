n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

nl = list(range(1, n+1))
edges.sort(key=lambda x: x[1])
for i, _ in edges:
    nl[i-1], nl[i] = nl[i], nl[i-1]

total = 0

for i in range(n-1):
    for j in range(n-1-i):
        if nl[j] > nl[j+1]:
            nl[j], nl[j+1] = nl[j+1], nl[j]
            total += 1
print(total)