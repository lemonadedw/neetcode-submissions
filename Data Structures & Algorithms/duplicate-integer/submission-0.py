class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = set()
        for i in nums:
            if i in nums_seen:
                return True
            else: nums_seen.add(i)
        return False

    # time complexity: O(N)
    # space complexity: O(N)