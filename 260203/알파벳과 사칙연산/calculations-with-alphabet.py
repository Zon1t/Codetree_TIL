expression = input()

# Please write your code here.
num_list = []
length = len(expression)

def backtrack(temp_list):
    if len(temp_list) == 6:
        num_list.append(temp_list[:])
        return
    for i in range(1, 5):
        temp_list.append(i)
        backtrack(temp_list)
        temp_list.pop()
backtrack([])

answer_list = []
for num_comb in num_list:
    num_dict = {alph:num for alph, num in zip(['a', 'b', 'c', 'd', 'e', 'f'], num_comb)}
    temp_num = num_dict[expression[0]]
    for i in range(length//2):
        if expression[i*2+1] == '+':
            temp_num += num_dict[expression[2*(i+1)]]
        elif expression[i*2+1] == '-':
            temp_num -= num_dict[expression[2*(i+1)]]
        else:
            temp_num *= num_dict[expression[2*(i+1)]]
    answer_list.append(temp_num)
print(max(answer_list))