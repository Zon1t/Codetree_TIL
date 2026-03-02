n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

store_dict = dict()

for num in arr:
    key_list = list(store_dict.keys())
    for key in key_list:
        store_dict[key+num] = store_dict.get(key+num, 0) + store_dict[key]
    store_dict[num] = store_dict.get(num, 0) + 1

print(store_dict[k])