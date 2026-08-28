''' 바이러스 실험 / 20260828 / 체감 난이도 : 골드 4
소요 시간 : 55분 / 시도 : 2회(1회차 : 시간 초과) / 실행 시간 : 1638ms / 메모리 : 24MB

타임 라인 : 구상(9분) - 구현(24분) - 검증(5분) - 재구상(4분) - 수정(10분) - 검증(3분)


[구상]
    - 예전에 플어봤던 원자 충돌 문제처럼 데이터 관리 등이 중요한 문제라고 생각했다.
    - 시간에 대해서 아주 깊게 고민하진 않고 넘어갔었다. n이 10짜리기도 하고 전역으로 관리하다보면
    꽤나 널널한 과정이라고 생각했었다.
    - 입력을 받고 함수를 정의하며 대략적인 코드의 틀을 만들어나갔다.

[구현]
    - 구현하는 과정에서도 큰 어려움은 없었다. 미리 생각해둔 전역 변수들과 함수와 상호작용하며, 그때그때
    필요한 기능들을 채워나갔다.
    - 최초에 바이러스를 죽이고 양분을 업데이트 하는 것을 1번 과정에 포함했었는데, 이걸 분리해야 내가 보기
    편할 것이라 생각했고, 이 기능을 분리하게 되었다.

[검증]
    - 각 단계별 변수가 정확하게 변화하는지 등을 확인했고, 해당 과정이 정확하다고 판단해서 곧바로 제출하게
    되었다.

[재구상]
    - 수정할 부분은 금방 보였던 것 같다. 예전에 팀원들에게 너무 heap 자료 남발하면 안좋을 수 있다고 했는데
    내가 딱 그 꼴을 당해버렸다;;; B형 준비할 때 버킷으로 heap 데이터 관리하는 유형의 문제가 생각났었는데
    그 생각과 함께 그냥 아무 생각 없이 heap을 사용했던 것 같다. 자료구조에 대한 고민은 몇번을 해도 손해가
    없는 것 같다.
    - 그리고 구현 단계에서 수정했던 바이러스 죽이는 로직도 먹는 로직에 합쳐 시간을 줄이려고 계획했다.
    - 추가적으로 시간을 줄일 수 있는 부분에 대한 고민을 진행했다.

[수정]
    - 힙을 리스트로 바꾸고, 쓰기 직전에만 sort하는 방식으로 진행했다.
    - 계획했던대로 1, 2번 함수를 합쳐서 구현했다.

[검증]
    - 추가적으로 시간을 줄일 수 있는 부분에 대해서 고민해보았다. 사실 이 정도면 시간 초과 안 나겠지라는 감이
    정확하지도 않고, 큰 케이스를 만들어 time을 찍어본 들 그게 절대적이지는 않아서 제출 전까지도 혹시나 하는
    마음이 있었다. 다행히 통과는 되었지만, 더 정리해볼 필요는 있을 것 같다.


* 피드백
    - 자료구조에 대한 고민은 몇 번을 해도 손해가 없다. 조금 더 고민하고 신중하게 사용하자.
'''

# 전체 양분을 관리해야 하므로 grid를 직접 그리는 방법 채택
# 바이러스는 따로 dictionary로 관리해도 될 것 같다.

# 시간초과 발생; 너무 대충 관리했나 싶기도 하다. 줄일 수 있는 부분이 있을까?
# 힙쓰지 말기 -> 귀찮아도 걍 필요할 때 sort해주자.

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def eat():
    # 양분을 섭취하는 로직.
    for row, col in list(virus_dict.keys()):
        new_dict = dict()
        yangboon, is_dead = 0, False
        for age in sorted(virus_dict[(row, col)]):
            cnt = virus_dict[(row, col)][age]

            if is_dead:
                yangboon += (age//2)*cnt
                continue

            threshold = yangboon_grid[row][col]+5+update_grid[row][col]*t
            if age*cnt <= threshold:
                new_dict[age+1] = cnt
                if (age+1)%5 == 0:
                    age_5[(row, col)] = age_5.get((row, col), 0) + cnt
                yangboon_grid[row][col] -= age*cnt
                threshold -= age * cnt
            elif age > threshold:
                is_dead = True
                yangboon += (age//2) * cnt
            else:
                nxt_cnt = threshold//age
                new_dict[age+1] = nxt_cnt
                if (age+1)%5 == 0:
                    age_5[(row, col)] = age_5.get((row, col), 0) + nxt_cnt
                yangboon_grid[row][col] -= age * nxt_cnt

                is_dead = True
                yangboon += (age//2) * (cnt-nxt_cnt)

        yangboon_grid[row][col] += yangboon

        if new_dict:
            virus_dict[(row, col)] = new_dict
        else:
            virus_dict.pop((row, col))

def burnsick():
    # 번식시키기
    for row, col in age_5:
        for d in range(8):
            next_row, next_col = row + dr[d], col + dc[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if (next_row, next_col) in virus_dict:
                virus_dict[(next_row, next_col)][1] = virus_dict[(next_row, next_col)].get(1, 0) + age_5[(row, col)]
            else:
                virus_dict[(next_row, next_col)] = {1: age_5[(row, col)]}
    # 다 번식했으면 비우기
    age_5.clear()

def count_virus():  # 여길 안고쳤었네
    answer = 0
    for d in virus_dict.values():
        answer += sum(d.values())
    return answer

N, K, T = map(int, input().split())
update_grid = [list(map(int, input().split())) for _ in range(N)]
yangboon_grid = [[0]*N for _ in range(N)]
virus_dict = dict()
for _ in range(K):
    row, col, age = map(int, input().split())
    row, col = row-1, col-1

    if (row, col) in virus_dict:
        if age in virus_dict[(row, col)]:
            virus_dict[(row, col)][age] += 1
        else:
            virus_dict[(row, col)][age] = 1
    else:
        virus_dict[(row, col)] = {age: 1}

# 5의 배수 나이를 가진 바이러스를 업데이트하기 위함.
age_5 = dict()
for t in range(T):
    # 1. 양분 먹기 및 바이러스 정리
    eat()

    # 2. 번식 진행
    burnsick()

    # 조기 종료?
    if not virus_dict:
        break

# 3. 정답 연산 후 출력
answer = count_virus()
print(answer)