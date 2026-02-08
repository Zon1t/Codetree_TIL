N = int(input())

# Please write your code here.

nl = [1, 1]
for i in range(2, N):
    nl.append(nl[-1]+nl[-2])

print(nl[N-1])