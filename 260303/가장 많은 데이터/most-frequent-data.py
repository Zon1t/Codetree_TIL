n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

cnt_dict = dict()
max_cnt = 0

for word in words:
    if word in cnt_dict:
        cnt_dict[word] += 1
        if max_cnt < cnt_dict[word]:
            max_cnt = cnt_dict[word]
    else:
        cnt_dict[word] = 1

print(max_cnt)