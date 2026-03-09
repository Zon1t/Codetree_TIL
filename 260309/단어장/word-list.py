import heapq

nl = []
data = dict()
for i in range(1, 1+int(input())):
    string = input()
    if data.get(string):
        data[string] += 1
    else:
        data[string] = 1
        heapq.heappush(nl, string)
while nl:
    string = heapq.heappop(nl)
    print(string, data[string])