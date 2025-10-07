import heapq
from typing import List


def kth_smallest(numsList : List[int], k:int)->int:

    min_heap = []

    for num in numsList:
        heapq.heappush(min_heap,num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

def kth_largest(numsList : List[int], k:int)->int:
    max_heap = []

    for num in numsList:
        heapq.heappush(max_heap,-num)
        if len(max_heap) >k:
            heapq.heappop(max_heap)
    return -max_heap[0]


nums = [3,2,1,5,6,4]
k = 2

print(kth_smallest(nums,k))
print(kth_largest(nums,k))