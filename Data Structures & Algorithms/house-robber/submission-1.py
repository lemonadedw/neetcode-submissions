class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i: int):
            if i in memo:
                return memo[i]

            if i > len(nums) - 1:
                return 0
            
            result = max(nums[i] + dfs(i + 2), dfs(i + 1))
            memo[i] = result
            return result
        
        return dfs(0)
        