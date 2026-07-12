class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        result = []

        for i in range(0, k):
            heapq.heappush(max_heap, -nums[i])
        
        result.append(-max_heap[0])

        for i in range(1, len(nums) - k + 1):
            if -nums[i - 1] == max_heap[0]:
                heapq.heappop(max_heap)
            else:
                max_heap.remove(-nums[i - 1])

            heapq.heappush(max_heap, -nums[i + k - 1])
            
            result.append(-max_heap[0])
        
        return result


        
        