K, N = map(int, input().split())

# Please write your code here.

def find_3(temp_list):
    max_cnt = 0
    cnt = 1
    for i in range(len(temp_list)):
        if i != 0 and temp_list[i] == temp_list[i-1]:
            cnt += 1
        else:
            max_cnt = max_cnt if cnt < max_cnt else cnt
    max_cnt = max_cnt if cnt < max_cnt else cnt
    return max_cnt >= 3

def backtrack(temp_list):
    if len(temp_list) == N:
        if find_3(temp_list):
            pass
        else:
            print(*(temp_list))
        return
    for i in range(1, 1+K):
        temp_list.append(i)
        backtrack(temp_list)
        temp_list.pop()
backtrack([])