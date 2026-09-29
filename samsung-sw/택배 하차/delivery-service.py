# 옛날 코드
def erase(h, w, r, c):
    for row in range(r, r+h):
        for col in range(c, c+w):
            grid[row][col] = 0


def check_fall(w, r, c):
    temp_list = []
    if 0 <= r-1:
        for col in range(c, c+w):
            if grid[r-1][col] != 0 and grid[r-1][col] not in temp_list:
                temp_list.append(grid[r-1][col])
    
    if temp_list:
        for key in temp_list:
            erase(blocks[key][0], blocks[key][1], blocks[key][2], blocks[key][3])
            fall(key, blocks[key][0], blocks[key][1], blocks[key][2], blocks[key][3])


def fall(k, h, w, r, c):
    for i in range(r, N-h+1):
        check = False
        for j in range(w):
            if i+h == N or grid[i+h][c+j] != 0:
                check = True
        if check:
            for row in range(i, i+h):
                for col in range(c, c+w):
                    grid[row][col] = k
            blocks[k] = (h, w, i, c)
            break
    check_fall(w, r, c)


def can_slide(direction, key):
    h, w, r, c = blocks[key]

    if direction:
        for col in range(c+w, N):
            if grid[r][col] or grid[r+h-1][col]:
                return False
        return True
    else:
        for col in range(c-1, -1, -1):
            if grid[r][col] or grid[r+h-1][col]:
                return False
        return True


N, M = map(int, input().split())
grid = [[0]*N for _ in range(N)]

blocks = dict()
for _ in range(M):
    k, h, w, c = map(int, input().split())
    fall(k, h, w, 0, c-1)
blocks = dict(sorted(blocks.items()))

for i in range(M):
    for j in blocks:
        if can_slide(i%2, j):
            erase(blocks[j][0], blocks[j][1], blocks[j][2], blocks[j][3])
            check_fall(blocks[j][1], blocks[j][2], blocks[j][3])
            blocks.pop(j)
            print(j)
            break
