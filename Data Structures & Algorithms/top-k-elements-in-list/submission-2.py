from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        min_heap = []

        for num in count:
            if len(min_heap) < k:
                heappush(min_heap, (count[num], num))
            elif count[num] > min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (count[num], num))
        
        result = []
        for i in range(k):
            result.append(min_heap[i][1])
        return result

        