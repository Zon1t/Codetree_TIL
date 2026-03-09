import heapq

N = int(input())
num_list = list(map(int, input().split()))
heap = []
heap.append(num_list.pop())
total = heap[0]
count = 1
answer = 0
while num_list:
    temp = num_list.pop()
    total += temp
    heapq.heappush(heap, temp)
    answer = max(answer, (total-heap[0])/count)
    count += 1

print(f'{answer:.2f}')