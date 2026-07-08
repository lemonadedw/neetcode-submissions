class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}

        for i, n in enumerate(nums):
            mapped[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapped and mapped[diff] != i:
                return [i, mapped[diff]]
        
        return []