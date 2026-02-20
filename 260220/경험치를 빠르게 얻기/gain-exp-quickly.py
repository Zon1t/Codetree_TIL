N, M = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

# 경험치를 기준으로 잡기에는 정확히 M만큼 얻어야 하는 것이 아닌, M 이상을 얻으면 되는 것이기 때문에
# 시간을 기준으로 문제를 해결해보는 편이 좋아보인다.
# 시간을 기준으로 dp형성.(최대가 100*100) idx가 커질수록 값이 당연히 커진다. -> 정렬되어있다.
# 이진탐색을 통해 M이상이 되는 지점을 select하면 될 것 같다!

dp = [0] * 10001

for j in range(N):
    for i in range(10000, quests[j][1]-1, -1):
        dp[i] = max(dp[i], dp[i-quests[j][1]]+quests[j][0])

start = 0
end = 10000
while start < end:
    mid = (start+end)//2
    if dp[mid] < M:
        start = mid + 1
    else:
        end = mid
if dp[-1] < M:
    print(-1)
else:
    print(start)