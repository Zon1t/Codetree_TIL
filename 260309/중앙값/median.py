import heapq

def update_heap(i, num):
    if i:
        heapq.heappush(heap_max, num)
    else:
        heapq.heappush(heap_min, -num)
    if heap_max and heap_max[0] < -heap_min[0]:
        temp1 = heapq.heappop(heap_max)
        temp2 = -heapq.heappop(heap_min)
        heapq.heappush(heap_max, temp2)
        heapq.heappush(heap_min, -temp1)

for _ in range(int(input())):
    num = int(input())
    num_list = list(map(int, input().split()))
    heap_min = []
    heap_max = []
    for i in range(len(num_list)):
        num = num_list[i]
        temp = i%2
        update_heap(temp, num)
        if not temp:
            print(-heap_min[0], end=' ')
    print()