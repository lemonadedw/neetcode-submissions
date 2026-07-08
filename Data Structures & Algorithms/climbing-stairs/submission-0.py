class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return i == n
            
            result = dfs(i + 1) + dfs(i + 2)
            memo[i] = result
            return result

        return dfs(0)