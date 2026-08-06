def can_upgrate(num):
    temp = 0
    for a in lst:
        temp += max(0, num-a) ** 2
        if B < temp:
            return False
    return True

def parametric_search(s, e):
    start, end = s, e
    while start < end:
        mid = (start+end) // 2
        if can_upgrate(mid):
            if start == mid:
                if can_upgrate(end):
                    return end
                else:
                    return start
            start = mid
        else:
            end = mid - 1
    return start

N, B = map(int, input().split())
lst = list(map(int, input().split()))
print(parametric_search(0, int(1e18)))