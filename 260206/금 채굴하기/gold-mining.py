n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def make_rhombus(K):
    return [(dr, dc) for dr in range(-K, K+1) for dc in range(-K, K+1) if abs(dr)+abs(dc)<=K]
def count_gold(row, col, rhombus):
    temp = 0
    for dr, dc in rhombus:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
            temp += 1
    return temp

max_gold = 0
for K in range(n+1):
    drcs = make_rhombus(K)
    for row in range(n):
        for col in range(n):
            gold = count_gold(row, col, drcs)
            if K**2+(K+1)**2 <= gold*m:
                max_gold = gold if max_gold < gold else max_gold
print(max_gold)