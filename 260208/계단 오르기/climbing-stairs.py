N = int(input())

# Please write your code here.

nl = [0, 0, 1, 1, 1]
for i in range(5, N+1):
    nl.append((nl[-2] + nl[-3])%10007)
print(nl[N])