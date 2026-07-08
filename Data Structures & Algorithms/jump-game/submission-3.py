class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        memo = {}

        def dfs(index) -> bool:
            if index >= target:
                return True

            if index in memo:
                return memo[index]

            result = False
            for i in range(index + 1, index + nums[index] + 1):
                result = result or dfs(i)
            
            memo[index] = result
            return result
        
        return dfs(0)