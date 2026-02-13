N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.

import sys
sys.setrecursionlimit(10000)
INT_MAX = sys.maxsize

memo = [-1] * (M+1)

def get_min_cnt(num):
    if memo[num] != -1:
        return memo[num]
    
    if num == M:
        memo[num] = 0
        return 0
    
    min_cnt = INT_MAX

    for coin in coins:
        if num + coin <= M:
            min_cnt = min(min_cnt, get_min_cnt(num+coin)+1)
    
    memo[num] = min_cnt
    return min_cnt

answer = get_min_cnt(0)

if answer == INT_MAX:
    print(-1)
else:
    print(answer)