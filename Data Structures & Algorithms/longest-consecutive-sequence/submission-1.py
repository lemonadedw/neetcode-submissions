class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        
        if len(nums) == 1:
            return 1

        count = 1
        max_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                count += 1
                print(nums[i], count)
            else:
                max_count = max(max_count, count)
                count = 1

        
            
        return max(max_count, count)