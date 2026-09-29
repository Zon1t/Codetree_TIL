class Box:
    def __init__(self, num, h, w, r, c):
        self.num = num
        self.height = h
        self.width = w
        self.row = r
        self.col = c
        self.is_out = False
        self.drop()
        self.draw()

    def get_data(self):
        return self.row, self.col, self.height, self.width

    def draw(self):
        for row in range(self.row, self.row+self.height):
            for col in range(self.col, self.col+self.width):
                grid[row][col] = self.num

    def erase(self):
        for row in range(self.row, self.row+self.height):
            for col in range(self.col, self.col+self.width):
                grid[row][col] = 0

    def drop(self):
        check_row = self.row+self.height
        while True:
            for col in range(self.col, self.col+self.width):
                if check_row >= N or grid[check_row][col]:
                    self.row = check_row-self.height
                    return
            check_row += 1

    def check_above(self):
        check_gravity = set()
        check_row = self.row-1
        if 0 <= check_row:
            for col in range(self.col, self.col+self.width):
                if grid[check_row][col]:
                    check_gravity.add(grid[check_row][col])
        return check_gravity

    def check(self, is_right):
        curr_col = self.col + (self.width if is_right else -1)
        lower = self.row+self.height-1      # 아래만 확인하면 되더라.
        while True:
            if curr_col < 0 or curr_col >= N:
                return True

            if grid[lower][curr_col]:
                return False

            curr_col += 1 if is_right else -1

    def get_out(self):
        self.erase()
        self.is_out = True


def print_grid():
    print(f'----grid----')
    for row in grid:
        print(*row)


# =============================================================
# 세팅

N, M = map(int, input().split())
grid = [[0]*N for _ in range(N)]

boxes = []
for idx in range(M):
    k, h, w, c = map(int, input().split())
    boxes.append(Box(k, h, w, 0, c-1))

boxes.sort(key=lambda x: x.num)

num_to_idx = {box.num: idx for idx, box in enumerate(boxes)}
answer = []

# =============================================================
# 실행부

for turn in range(M):
    for box in boxes:
        if box.is_out:
            continue

        # 치울 수 있는지 체크!
        can_erase = box.check(turn%2)
        if not can_erase:
            continue

        # 이때 항상 내 위에 있는 박스들에 대해서 생각해야 한다.
        box.get_out()
        drop_set = box.check_above()
        while drop_set:
            new_drop_set = set()
            for box_num in drop_set:
                # 현재 박스 찾기
                box_idx = num_to_idx[box_num]
                curr_box = boxes[box_idx]

                # 추가로 체크할 박스 업데이트
                need_check = curr_box.check_above()
                new_drop_set |= need_check

                # 박스 지우고, 떨구고, 그리기
                curr_box.erase()
                curr_box.drop()
                curr_box.draw()

            # 드롭셋 업데이트
            drop_set = new_drop_set

        answer.append(str(box.num))
        break

# 정답 출력
print('\n'.join(answer))