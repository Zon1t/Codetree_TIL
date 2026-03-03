n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

store_dict = dict()
count = 0

for num in arr:
    store_dict[num] = store_dict.get(num, 0) + 1

for key in store_dict:
    count += store_dict[key] * store_dict.get(k-key, 0)

if not k%2 and (k//2 in store_dict):
    count -= store_dict[k//2]

print(count//2)