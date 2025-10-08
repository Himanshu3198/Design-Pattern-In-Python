import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        max_heap = []

        for num, count in freq.items():
            heapq.heappush(max_heap, (-count, num))

        result = []

        while (len(max_heap) > 0 and k > 0):
            freq, num = heapq.heappop(max_heap)
            result.append(num)
            k -= 1

        return result
