n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.

hashmap = dict()

for command in commands:
    v = command[0]
    if v == 'add':
        hashmap[command[1]] = command[2]
    elif v == 'remove':
        hashmap.pop(command[1])
    else:
        value = hashmap.get(command[1], None)
        if value is None:
            print(None)
        else:
            print(value)