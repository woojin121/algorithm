import heapq
import sys

n = int(input())

heap = []
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp != 0:
        heapq.heappush(heap, -tmp)
    else:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)