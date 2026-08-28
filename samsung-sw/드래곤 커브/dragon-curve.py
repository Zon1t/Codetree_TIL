def in_range(row, col):
    return 0 <= row <= 100 and 0 <= col <= 100

def draw(sr, sc, d, g):
    draw_lst.clear()
    delta_lst.clear()

    draw_lst.append((sr, sc))
    curr_row, curr_col = sr+dr[d], sc+dc[d]
    visited[curr_row][curr_col] = True

    for _ in range(g):
        for row, col in draw_lst:
            delta_lst.append((curr_row - row, curr_col - col))

        for delta_r, delta_c in delta_lst:
            next_row, next_col = curr_row - delta_c, curr_col + delta_r
            if in_range(next_row, next_col):
                visited[next_row][next_col] = True
            draw_lst.append((next_row, next_col))

        draw_lst.append((curr_row, curr_col))
        curr_row, curr_col = curr_row - (curr_col - sc), curr_col + (curr_row - sr)
        visited[curr_row][curr_col] = True
        delta_lst.clear()


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

visited = [[False] * 101 for _ in range(101)]

draw_lst, delta_lst = [], []
for _ in range(int(input())):
    r, c, d, g = map(int, input().split())
    visited[r][c] = True
    draw(r, c, d, g)

answer = 0
for row in range(100):
    for col in range(100):
        if visited[row][col] and visited[row+1][col] and visited[row][col+1] and visited[row+1][col+1]:
            answer += 1

print(answer)