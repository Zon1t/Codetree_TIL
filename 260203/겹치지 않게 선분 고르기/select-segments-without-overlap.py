n = int(input())
line_list = []

for _ in range(n):
    line_list.append(tuple(map(int, input().split())))
line_list.sort(key = lambda x: x[1])
# Please write your code here.

line = [False] * 1001
count = 0
for A, B in line_list:
    if sum(line[A:B+1]):
        continue
    else:
        for i in range(A, B+1):
            line[i] = True
        count += 1
print(count)