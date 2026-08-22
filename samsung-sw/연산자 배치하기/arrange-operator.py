N = int(input())

nlst = list(map(int, input().split()))
olst = list(map(int, input().split()))

def calc_(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    else:
        return num1 * num2

def backtrack(cum, idx):
    global min_, max_
    if idx == N:
        if cum < min_:
            min_ = cum
        if cum > max_:
            max_ = cum
        return

    for i in range(3):
        if not olst[i]:
            continue
        olst[i] -= 1
        backtrack(calc_(cum, nlst[idx], i), idx+1)
        olst[i] += 1


min_ = int(1e9)
max_ = -int(1e9)

backtrack(nlst[0], 1)
print(min_, max_)