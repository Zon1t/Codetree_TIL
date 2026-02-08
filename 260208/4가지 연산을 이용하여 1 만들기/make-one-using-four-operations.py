N = int(input())

# Please write your code here.

from collections import deque

answer = -1
num_set = set()
q = deque([(N, 0)])
num_set.add(N)
while q:
    num, t = q.popleft()
    if num == 1:
        answer = t
        break
    if num+1 not in num_set:
        q.append((num+1, t+1))
        num_set.add(num+1)
    if num-1 not in num_set:
        q.append((num-1, t+1))
        num_set.add(num-1)
    if not num%2:
        if num//2 not in num_set:
            q.append((num//2, t+1))
            num_set.add(num//2)
    if not num%3:
        if num//3 not in num_set:
            q.append((num//3, t+1))
            num_set.add(num//3)
print(answer)