N = int(input())
data = []
for _ in range(N):
    name, height, age = input().split()
    data.append((name, height, age))
data.sort(key = lambda x:x[1])

for datum in data:
    print(*datum)