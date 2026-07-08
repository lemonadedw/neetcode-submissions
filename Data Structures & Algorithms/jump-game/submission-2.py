class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        def dfs(index) -> bool:
            if index >= target:
                return True

            result = False
            for i in range(index + 1, index + nums[index] + 1):
                result = result or dfs(i)
            
            return result
        
        return dfs(0)