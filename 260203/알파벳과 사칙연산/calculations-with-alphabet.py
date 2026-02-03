expression = input()

# Please write your code here.
num_list = []
length = len(expression)

def backtrack(temp_list):
    if len(temp_list) == length // 2 + 1:
        num_list.append(temp_list[:])
        return
    for i in range(1, 5):
        temp_list.append(i)
        backtrack(temp_list)
        temp_list.pop()
backtrack([])

answer = -2**31
for num_combination in num_list:
    temp_num = num_combination[0]
    idx = 1
    for iterator in expression[1::2]:
        if iterator == '-':
            temp_num -= num_combination[idx]
        elif iterator == '+':
            temp_num += num_combination[idx]
        else:
            temp_num *= num_combination[idx]
        idx += 1
    answer = max(answer, temp_num)
print(answer)