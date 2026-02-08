n = int(input())

# Please write your code here.

nl = [0, 1, 3]
for i in range(3, n+1):
    nl.append((nl[-1] + 2*nl[-2])%10007)
print(nl[n])