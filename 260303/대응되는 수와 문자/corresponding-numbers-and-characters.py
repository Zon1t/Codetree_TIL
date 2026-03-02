n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.

num_to_string = dict()
string_to_num = dict()

for idx in range(1, n+1):
    num_to_string[idx] = words[idx]
    string_to_num[words[idx]] = idx

for query in queries:
    if query.isnumeric():
        print(num_to_string[int(query)])
    else:
        print(string_to_num[query])