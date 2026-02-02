n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def find_max(temp_list, capacity):
    max_value = -1
    list_length = len(temp_list)
    for start in range(list_length):
        for end in range(start, start+m):
            temp_value = 0
            if sum(temp_list[start:end+1]) <= capacity:
                for w in temp_list[start:end+1]:
                    temp_value += w**2
                max_value = max(max_value, temp_value)
            else:
                break
    return max_value

# 서로 다른 행을 선택했을 경우
# -> 각 행에서 투포인터 사용시 최댓값 선택 후 리스트 저장
# 리스트에서 가장 큰 두 값 더하기

max_row = []
for each_row in weight:
    max_row.append(find_max(each_row, c))
max_row.sort()
first_case_max = max_row[-1] + max_row[-2]


# 서로 같은 행을 선택했을 경우. 모든 가능한 투포인터 선택 경우에 대해서
# 그 부분 제외하고 또 투포인터 쓰기..?

second_case_max = -1
max_row = []
for each_row in weight:
    max_value = -1
    for start in range(n):
        for end in range(start, start+m):
            temp_sum = 0
            if sum(each_row[start:end+1]) <= c:
                for w in each_row[start:end+1]:
                    temp_sum += w**2
                temp_sum += max(find_max(each_row[:start], c), find_max(each_row[end+1:], c))
                max_value = max(max_value, temp_sum)
            else:
                break
    max_row.append(max_value)
second_case_max = max(max_row)
print(max(first_case_max, second_case_max))