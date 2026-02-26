n = int(input())

# Please write your code here.

nl = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
mod = 10**9+7
for _ in range(n-1):
    nl[0], nl[1], nl[2], nl[3], nl[4], nl[5], nl[6], nl[7], nl[8], nl[9] = nl[1], nl[0] + nl[2], nl[1] + nl[3], nl[2] + nl[4], nl[3] + nl[5], nl[4] + nl[6], nl[5] + nl[7], nl[6] + nl[8], nl[7] + nl[9], nl[8]
    for i in range(10):
        nl[i] %= mod
total = 0
for i in range(10):
    total += nl[i]
    total %= mod
print(total)