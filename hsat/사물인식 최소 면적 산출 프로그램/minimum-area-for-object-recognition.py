N, K = map(int, input().split())

arr = [[] for _ in range(K)]

for _ in range(N):
    r, c, color = map(int, input().split())
    arr[color-1].append((r, c))

answer = 2000 * 2000 + 1

def backtrack(idx, min_r, min_c, max_r, max_c):
    global answer
    area = (max_r-min_r) * (max_c-min_c)
    if answer <= area:
        return

    if idx == K:
        if area < answer:
            answer = area
        return


    for r, c in arr[idx]:
        backtrack(idx+1, min(min_r, r), min(min_c, c), max(max_r, r), max(max_c, c))

backtrack(0, 1000, 1000, -1000, -1000)
print(answer)