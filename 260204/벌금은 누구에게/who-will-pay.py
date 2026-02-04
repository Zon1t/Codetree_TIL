N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
answer = -1
nl = [0] * (N+1)
for s in student:
    nl[s] += 1
    if nl[s] == K:
        answer = s
        break
print(answer)