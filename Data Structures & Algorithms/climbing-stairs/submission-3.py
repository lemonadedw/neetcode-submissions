from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]

        #     if i >= n:
        #         return i == n
            
        #     result = dfs(i + 1) + dfs(i + 2)
        #     memo[i] = result
        #     return result

        # return dfs(0)

        if n <= 2:
            return n * 1
        
        dp = deque([1, 1])

        for i in range(n - 2, -1, -1):
            dp.appendleft(dp[-1] + dp[-2])
            dp.pop()

        return dp[0]