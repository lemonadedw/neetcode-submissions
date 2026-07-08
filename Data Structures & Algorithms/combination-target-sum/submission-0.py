class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(idx: int, cur_sum: int, sub: List[int]):
            if cur_sum == target:
                res.append(sub.copy())
                return
            if idx >= len(nums) or cur_sum > target:
                return
            
            sub.append(nums[idx])
            backtrack(idx, cur_sum + nums[idx], sub)
            sub.pop()
            backtrack(idx + 1, cur_sum, sub)


        backtrack(0, 0, [])

        return res
        