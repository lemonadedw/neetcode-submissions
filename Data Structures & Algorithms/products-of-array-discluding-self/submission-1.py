class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [nums[0]]
        for i in range(1, len(nums)):
            forward.append(nums[i] * forward[i - 1])
        
        back = [0] * len(nums)
        back[-1] = nums[-1]

        # 4, 4x3, 4x3x2, 4x3x2x1
        for i in range(len(nums) - 2, -1, -1):
            back[i] = nums[i] * back[i + 1]
        
        result = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                result[0] = back[i + 1]
            elif i == len(nums) - 1:
                result[-1] = forward[i - 1]
            else:
                result[i] = forward[i - 1] * back[i + 1]

        return result