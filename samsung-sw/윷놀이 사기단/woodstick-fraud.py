''' 윷놀이 사기단 / 20260903 / 체감 난이도 : 골드 3
소요 시간 : 2시간 55분 / 시도 3회 (1, 2회 : 틀림) / 실행 시간 : 825ms / 메모리 : 26MB

타임 라인 : 구상(13분) - 구현(20분) - 검증(5분) - 디버깅 1차(21분) - 구현 2차 및 디버깅(1시간 56분)


[구상]
    - 판을 어떻게 구성할까? 인덱스로 쭉 늘려서 도착 인덱스에서 옮겨준다거나, 여러개의 경로를 만들어
    경로별로 말을 관리하는 등의 생각을 했던 것 같다. 나는 경로 여러 개를 리스트화해서 경로별로 말을
    관리 해야겠다 생각했다.
    - 백트래킹을 사용하면 곧바로 문제를 풀 수 있을 것이라 생각했다. 파란색 칸 위의 숫자 / 겹치는
    숫자 정도만 주의하면 될 것 같다.

[구현]
    - 구현 과정도 큰 문제가 없었다. 혹시 헷갈릴까봐 분기문을 여럿 나눠서 분기별로 확실하게 처리하고
    자 했다. 겹치는 말에 대한 체크 로직도 여럿 검증해보았다.
    - 분기마다 문제와 비교하며 적절하게 처리했는지 확인해보았다.

[검증]
    - 구현 과정에서 많이 검증해보았다 생각했고 테케 확인 후 제출해보았다.

[1차 디버깅]
    - 체크 로직이 잘못 구성되어 있음을 곧바로 알 수 있었다. 좀 더 확실하게 로직을 구성해보았다.
    - 적절한 로직 처리를 위해, 경로별 숫자 set에 대해 교집합을 찾아, 내가 구성한 분기문에서 모두
    올바르게 작동하는지 체크해보았다.
    - 그 밖의 부분은 일부 정리만 하고, 큰 문제가 없다고 판단하여 곧바로 제출해보았다.

[2차 구현(갈아 엎었음)]
    - 아예 처음부터 다시 시작했다. 판만 제대로 되어 있나 재차 검증하고, 판만 남겨두었다.
    - 처음 구상할 때 생각했었던 로직으로 구현해보았다. 파란칸 로직을 한 번에 처리하게 끔 했고,
    체크 로직도 조금 수정해보았다.
    - 겹치는 숫자에 대해서 재차 확인해, 내가 잘못한 부분이 있는가에 대해서 생각해보았다.
    - 이때 처음 틀린 테케를 들고와 답만 계속 확인해보았다. 전부 해당 테케에서 걸렸다.
    - 문제를 아예 잘못 이해했나 싶어서, 선택할 수 있는 숫자들 순서를 고려하지 않는 경우 등 혹시
    나 싶었던 모든 경우를 다 테스트해보았다. 그렇게 했을 때는 기존 테케들도 다 틀리게 나와 내가
    반영하지 않은 조건에 대해서 더욱 따져가보았다.
    - 끝나고 나서까지 삽질하다, 잘 생각해보니 나간 말을 -1로 세팅해서 잘못된 로직을 수행하지 않
    을까 생각했고, 이를 수정하니 맞을 수 있었다. 백트래킹 내부 로직에서 처리를 한걸 전체적으로 다
    처리했다고 착각했었다. 그래서 문제를 재차 읽을 때에도 인지는 했지만, 이미 반영했다고 판단해
    넘어갔다.

* 피드백
    - 아예 나간 말을 처리할 떄 다른 방식으로도 해봤으면 어땠을까
    - 안 풀리면 좀 다른 방식으로, 변수를 다르게 가져가든 방식이든 뭐든 새로 해보면 좋을 것 같다.
'''
# 윷놀이 판을 어떻게 구성해야 할까? lst 4개를 만들어 grid를 업데이트 하는 방식으로
# 진행하면 좋을 것 같다.
# 던질 수 있는 횟수 10회 / 최댓값 구하는 문제. 4^10 정도? 백트래킹 하면 되겠다.
# 이동 불가능함 관리 -> 말의 위치를 저장하는 data_lst로 관리. 있으면 못가고 등등~
# 가지치기 조건 없나? 머리 아프니까 한 번 초기화 하고 가자.
# 원하는 이동 횟수 -> 이거 뭔말임??

grid = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
        [10, 13, 16, 19, 25, 30, 35, 40],
        [20, 22, 24, 25, 30, 35, 40],
        [30, 28, 27, 26, 25, 30, 35, 40]]
cnts = list(map(int, input().split()))

grid_length = [len(row) for row in grid]
chage_set = {10, 20, 30}
check_set = {25, 35, 40}

# 집합 찍어보기
# for i in range(4):
#     for j in range(i):
#         print(f'--------intersection{i, j}---------')
#         print(set(grid[i]).intersection(set(grid[j])))

# 말의 정보를 받는 lst. 어쨋든 말 하나 움직이는 것까지 고정. 따라서 0번말 이동시켜놓기.
# 별거 아닌 것 같지만 시간 많이 줄여줄듯?
info = [[0, 0] for _ in range(4)]
info[0] = [0, cnts[0]] if cnts[0] != 5 else [1, 0]

def check(grid_idx, pos, mal_idx):
    # 다른 말들에 대해서 진행.
    for another_idx in range(4):
        mal_grid, mal_pos = info[another_idx][0], info[another_idx][1]

        # 자신이거나, 이미 탈출한 말인 경우 스킵.
        if mal_idx == another_idx or mal_pos == -1:
            continue

        # 정확히 같은 격자, 같은 위치면 False
        if mal_grid == grid_idx and mal_pos == pos:
            return False
        # 정확히 같은 값인데.. 이건 좀 생각해봐야 함.
        if grid[mal_grid][mal_pos] == grid[grid_idx][pos]:
            # 누가 봐도 같은 위치면 False
            if grid[grid_idx][pos] in check_set:
                return False
            # 30인데 공통 경로의 30인 경우. 파랑30은 위에서 처리되었음.
            if grid[grid_idx][pos] == 30 and pos and mal_pos:
                return False

    # 무사히 통과했으면 True 반환
    return True

def backtrack(turn, acc):
    global answer
    # 종료 조건.
    if turn == 10:
        if answer < acc:
            answer = acc
        return

    # 각 말에 대해서 진행.
    for mal_idx in range(4):
        grid_idx, curr_pos = info[mal_idx][0], info[mal_idx][1]

        # 만약 이미 탈출한 말이면 건뛰.
        if curr_pos == -1:
            continue

        # 다음 위치를 탐색한다.
        next_pos = curr_pos + cnts[turn]

        # 만약 격자 밖을 벗어나면 무조건 도착지점.
        if next_pos >= grid_length[grid_idx]:
            info[mal_idx][1] = -1
            backtrack(turn+1, acc)
            info[mal_idx][1] = curr_pos
            continue

        # 그게 아니라면 격자 안에 존재.
        # 파란 칸인 경우. 격자 바꿔주자.
        if grid_idx == 0 and (grid[0][next_pos] in chage_set):
            if check(grid[0][next_pos]//10, 0, mal_idx):
                info[mal_idx] = [grid[0][next_pos]//10, 0]
                backtrack(turn+1, acc+grid[0][next_pos])
                info[mal_idx] = [0, curr_pos]
        # 파란 칸이 아닌 경우. 그냥 격자따라 ㄱㄱ
        else:
            if check(grid_idx, next_pos, mal_idx):
                info[mal_idx][1] = next_pos
                backtrack(turn+1, acc+grid[grid_idx][next_pos])
                info[mal_idx][1] = curr_pos

# 적절하게 백트래킹 진행
answer = 0
backtrack(1, grid[0][cnts[0]])

# 정답 출력
print(answer)
