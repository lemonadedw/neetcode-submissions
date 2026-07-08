class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            rob1, rob2 = 0, 0

            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
            
        return max(helper(nums[1:]), helper(nums[:-1]))