''' 생명과학부 랩 인턴 / 20260901 / 체감 난이도 : 골드 5
소요 시간 : 38분 / 시도 : 1회 / 실행 시간 : 274ms / 메모리 : 27MB

녹화가 안눌러져 있었습니다.. 쉽게쉽게 해결한 문제였어서 그나마 다행인 것 같긴 합니다..
다음부터는 녹화 체크 꼭 하기!


[구상]
    - 사실 너무 익숙한 문제라 데이터를 어떻게 관리해야 할지 머리에 금방금방 정리되었던 것 같습니다.
    - 수행해야 하는 기능들도 단순하다고 생각했어서 함수나 변수를 금방 정리하고 구현 단계로 넘어갔습니다.

[구현]
    - 구상 때와 일부 달라진 점이 있습니다. 막상 column 기준으로 실행을 하자니, grid를 만들지 않은
    풀이 방식에서 새로 dictionary를 만들까 고민을 했던 것 같습니다. dict_lst[col][row]처럼 col
    단위로 딕셔너리를 만드는 등? 해법을 떠올렸는데, 어짜피 move함수에서 좌표를 계산할 테니, 거기서
    다음 column에 있는 row들을 뽑아오자 생각이 들었습니다. row만 뽑아와도 dictionary 키값 접근이
    가능했기에 해당 부분은 잘한 부분이라 생각합니다.
    - 이동 규칙을 개미 때와 동일하다고 생각했는데, 막상 구현하려니 다르다는 사실을 알게 되었습니다.
    반사되는 기준이 개미 때는 벽이였고, 여기선 마지막 칸이다 보니 살짝 헷갈리는 구석이 있었습니다. 더
    불어 방향에 대해서도 결정의 해줘야 하다보니 다시 규칙성을 발견해야 했습니다. 다행히 전체를 그려보고,
    늘려보고 하면서 관찰하니 곧바로 규칙이 보였고 해당 로직을 금방 구현할 수 있었습니다.

[검증]
    - 매 순간 올바른 위치에 올바른 방향으로 존재하고, 먹는 로직이 정상적으로 동작함을 출력해보며 확인
    했습니다. 이후 문제와 다시 교차 검증을 해보고 제출했습니다.

'''

# 1. 열별 탐색 진행. 이때 채취 여부를 체크하면 좋을 것 같다.
# 2. 이동 진행. 이때 위치는 어떻게 연산하는가? 개미 문제를 떠올리면 너무 쉽게 구할 수 있다.
# 2-1. 만약 같은 공간에 곰팡이가 있으면 실시간으로 잡아먹게끔 세팅해주면 될 것이다.
# 3. 모든 열에 대해서 위 과정을 수행하고, 끝났을 때의 곰팡이 크기 총합 출력하기.
# 좌표랑 방향 모두 1부터 시작함에 유의하자.
# 딕셔너리 쓰면 금방 풀 수 있지 않을까?


# 순서대로 위, 아래, 오른, 왼
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


# 해당 위치에 있는 곰팡이를 채취하는 함수.
def catch(row, col):
    global answer
    _, _, size = gompang2.pop((row, col))
    answer += size

# 곰팡이를 이동시켜주자!
def move():
    global gompang2
    # 이동 이후 정보를 저장할 딕셔너리.
    new_pang2 = dict()
    # 다음 열에 있는 애들을 미리 저장해주기 위해 비워두기.
    catch_pang2.clear()

    # 존재하는 곰팡이들에 대해 순회.
    for curr_row, curr_col in gompang2:
        speed, curr_dir, size = gompang2[(curr_row, curr_col)]

        # 위/아래로 움직이는 경우
        if curr_dir <= 1:
            # 반복 주기 : 2N-2. 이를 활용해 다음 좌표 및 방향 연산.
            next_row = (curr_row + speed * dr[curr_dir]) % row_standard
            next_col = curr_col
            if next_row <= N-1:
                next_dir = curr_dir
            else:
                next_row = row_standard-next_row
                next_dir = curr_dir ^ 1
        # 좌/우로 움직이는 경우
        else:
            # 반복 주기 : 2M-2. 이를 활용해 다음 좌표 및 방향 연산.
            next_row = curr_row
            next_col = (curr_col + speed * dc[curr_dir])%col_standard
            if next_col <= M-1:
                next_dir = curr_dir
            else:
                next_col = col_standard-next_col
                next_dir = curr_dir ^ 1
        
        # 만약 다음 채취 대상이 되는 column에 있다면 기록해주자.
        if next_col == col+1:
            catch_pang2.append(next_row)
        
        # 만약 해당 위치에 이미 곰팡이가 있으면, 크기에 따라 업데이트 해주기.
        if (next_row, next_col) in new_pang2:
            if size > new_pang2[(next_row, next_col)][2]:
                new_pang2[(next_row, next_col)] = (speed, next_dir, size)
        # 없으면 그냥 적기
        else:
            new_pang2[(next_row, next_col)] = (speed, next_dir, size)

    # 업데이트
    gompang2 = new_pang2


# 입력받기
N, M, K = map(int, input().split())

# 움직이는 로직에서 사용할 변수들.
row_standard, col_standard = 2*N-2, 2*M-2

# 기록용 변수
gompang2, catch_pang2 = dict(), []
for _ in range(K):
    r, c, s, d, b = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    
    # 순회를 또 하긴 싫으니 미리 저장해두고 꺼내 쓰자.
    if c == 0:
        catch_pang2.append(r)
    
    # data 저장.
    gompang2[(r, c)] = (s, d, b)

# 채취할 때마다 업뎃 ㄱㄱ
answer = 0
# 실험 진행
for col in range(M):
    # 1. 곰팡이 채취. 해당 열에 채취할 곰팡이가 있으면 채취해주자.
    if catch_pang2:
        catch_pang2.sort()
        catch(catch_pang2[0], col)

    # 2. 곰팡이 움직이기.
    move()

print(answer)