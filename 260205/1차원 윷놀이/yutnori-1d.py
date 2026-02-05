n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

max_count = 0

def backtrack(idx, score_list):
    global max_count
    if idx == n:
        count = 0
        for score in score_list:
            if score >= m-1:
                count += 1
        max_count = max_count if count < max_count else count
        return
    for i in range(k):
        score_list[i] += nums[idx]
        backtrack(idx+1, score_list)
        score_list[i] -= nums[idx]

backtrack(0, [0]*k)
print(max_count)