n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def select_coins(start, cum_sum):
    if cum_sum == m:
        print('Yes')
        exit(0)
    if cum_sum > m:
        return
    for i in range(start, n):
        select_coins(i+1, cum_sum+A[i])

select_coins(0, 0)

print('No')