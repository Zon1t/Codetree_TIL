n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
A_list = [0] * (sum(t)+1)
now_pos = 0
temp = 0
for i in range(n):
    if d[i] == 'R':
        for i in range(1, t[i]+1):
            now_pos += 1
            temp += 1
            A_list[temp] = now_pos
    else:
        for i in range(1, t[i]+1):
            now_pos -= 1
            temp += 1
            A_list[temp] = now_pos

B_list = [0] * (sum(t)+1)
now_pos = 0
temp = 0
for i in range(m):
    if d2[i] == 'R':
        for i in range(1, t2[i]+1):
            now_pos += 1
            temp += 1
            B_list[temp] = now_pos
    else:
        for i in range(1, t2[i]+1):
            now_pos -= 1
            temp += 1
            B_list[temp] = now_pos
answer = -1
for i in range(1, len(A_list)):
    if A_list[i] == B_list[i]:
        answer = i
        break
print(answer)