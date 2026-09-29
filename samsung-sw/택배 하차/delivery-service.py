''' 택배 하차 / 20260929 / 체감 난이도 : 골드 4
소요 시간 : 46분 / 시도 : 1회 / 실행 시간 : 111ms / 메모리 : 19MB

타임 라인 : 구상(19분) - 구현(23분) - 검증(4분)


[구상]
    - 풀어본 것 같은 문제다 싶어서 확인해봤는데, 올해 2월에 풀어봤던 문제이다. 그래도 처음 풀어본
    다는 마음가짐으로 접근해보았다.
    - 클래스 풀이를 계획했다. 전체적으로 필요한 메서드나 실행부 일부를 정리해두고, 본격적인 구현에
    들어갔다.

[구현]
    - 딕셔너리를 쓰기 싫어서 boxes를 sort 때렸는데, 잘 생각해보니 idx <-> num이 가능해야 문제
    를 풀기 용이함을 깨달았다. 이미 멀리 와버렸어서 그냥 num_to_idx를 컴프리헨션으로 정의해서 이
    를 바탕으로 box에 접근했다.
    - 구현하면서 그냥 순차적으로 drop_set 업데이트 해가면서 진행해도 괜찮은가에 대해서 꽤나 많은
    고민을 했던 것 같다. 다양한 케이스를 만들어가면서 생각해보았는데, 어짜피 순차적으로 확인하는
    과정에서 특정 블럭에 대해 재차 확인하게 되니 큰 문제가 없음을 인지하고 넘어갔다.
    - N차 때나 리팩토링할 때 많이 연습해서 그런가 이런 문제에서는 클래스 적용해서 금방금방 해결할
    수 있게 된 것 같다.

[검증]
    - grid 찍어 보면서 매 턴마다 박스를 올바르게 제거하는지, 제거하는 과정에서 잔해물들이 grid에
    남지는 않았는지 등을 체크해보았다. 크게 에지랄게 있을까 싶었어서 테케 정도만 제대로 확인해보고
    문제 다시금 읽고, 코드 다시 쭉 따라가보고 제출해보았다.


'''
# 좌우 번갈아가면서 떨구기.. 연쇄 작용 잘 처리해야 할 듯.
# 클래스 써서 푸는게 제일 좋을 것 같기는 하다? 어떨지 모르겠다. 한 번 해볼까


class Box:
    def __init__(self, num, h, w, r, c):
        self.num = num
        self.height = h
        self.width = w
        self.row = r
        self.col = c
        self.is_out = False
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
        while True:
            if curr_col < 0 or curr_col >= N:
                return True

            for row in range(self.row, self.row+self.height):
                if grid[row][curr_col]:
                    return False

            curr_col += 1 if is_right else -1

    def get_out(self):
        self.erase()
        self.is_out = True


def drop(h, w, c, r=0):
    row = r+h
    while True:
        for col in range(c, c+w):
            if row >= N or grid[row][col]:
                return row-h
        row += 1


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
    r = drop(h, w, c-1)
    boxes.append(Box(k, h, w, r, c-1))
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

                # 박스 지우고,
                curr_box.erase()
                # 위치 잡아주고,
                row, col, height, width = curr_box.get_data()
                row = drop(height, width, col, row)
                boxes[box_idx].row = row
                # 새로 그려주기.
                boxes[box_idx].draw()

            # 체크셋 업데이트
            drop_set = new_drop_set

        answer.append(str(box.num))
        break

# 정답 출력
print('\n'.join(answer))