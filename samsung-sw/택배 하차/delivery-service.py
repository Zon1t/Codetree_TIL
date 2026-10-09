# []/
# 1. 택배 투입.
#       - 바로 아래칸 width만큼 확인해가며 떨구면 된다.
#       - 떨어지는 로직은 재사용할 것으로 보이니 적절하게 구성

# 2. 택배 하차
#       - 좌측, 우측을 번갈아가며 택배를 하차시킴.
#       - 하차 여부 판단이 먼저.
#       - 바로 상단에 있는 애들도 떨구기(연쇄)


class Box:
    def __init__(self, idx, height, width, col):
        self.idx = idx
        self.height = height
        self.width = width
        self.col = col
        self.row = self.drop()
        self.update(self.idx)
        self.out = False

    def drop(self, start_row=0):
        check_row = start_row + self.height
        while check_row < N:
            for col in range(self.col, self.col + self.width):
                if grid[check_row][col]:
                    return check_row - self.height
            check_row += 1
        return check_row - self.height

    def update(self, value):
        for row in range(self.row, self.row+self.height):
            for col in range(self.col, self.col+self.width):
                grid[row][col] = value

    def check_above(self):
        check_row, check_set = self.row-1, set()
        if check_row >= 0:
            for col in range(self.col, self.col+self.width):
                if grid[check_row][col]:
                    check_set.add(grid[check_row][col])
        return check_set

    def check_side(self, is_right):
        check_row = self.row + self.height - 1
        for col in (range(self.col-1, -1, -1) if not is_right else range(self.col+self.width, N)):
            if grid[check_row][col]:
                return False
        return True

    def get_out(self):
        check_set = self.check_above()
        self.update(0)
        self.out = True

        while True:
            if not check_set:
                break

            new_check = set()
            for box_idx in check_set:
                curr_box = box_info[box_idx]

                update_row = curr_box.drop(curr_box.row)
                if curr_box.row == update_row:
                    continue

                new_check.update(curr_box.check_above())

                curr_box.update(0)
                curr_box.row = update_row
                curr_box.update(curr_box.idx)
            check_set = new_check


# ====================================================================
# 세팅

N, M = map(int, input().split())
grid = [[0] * N for _ in range(N)]

box_info = dict()
indexes = []
for _ in range(M):
    k, h, w, c = map(int, input().split())
    box_info[k] = Box(k, h, w, c-1)
    indexes.append(k)

indexes.sort()
answer = []

# ====================================================================
# 실행부

for turn in range(M):
    for box_idx in indexes:
        if box_info[box_idx].out:
            continue

        if box_info[box_idx].check_side(turn%2):
            box_info[box_idx].get_out()
            answer.append(str(box_idx))
            break

print('\n'.join(answer))