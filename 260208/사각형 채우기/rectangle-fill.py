N = int(input())

# Please write your code here.

nl = [0, 1, 2]
for i in range(3, N+1):
    nl.append((nl[-1]+nl[-2])%10007)
print(nl[N])