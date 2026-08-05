import bisect

def can_cover(length):
    cnt = 0
    now = lst[0]
    while cnt < K:
        nxt = now+length
        idx = bisect.bisect_left(lst, nxt)
        if idx == N:
            return True
        now = lst[idx]
        cnt += 1
    return False

def parametric_search(start, end):
    s, e = start, end
    while s < e:
        mid = (s+e)//2
        if can_cover(mid):
            e = mid
        else:
            s = mid + 1
    return s

N, K = map(int, input().split())
lst = list(map(int, input().split()))
max_length = (lst[-1] - lst[0]) // K + 1
answer = parametric_search(1, max_length)
print(answer)