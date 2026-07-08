class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f, l = 0, len(numbers) - 1

        while numbers[f] + numbers[l] != target:
            if numbers[f] + numbers[l] > target:
                l -= 1
            else:
                f += 1

        return [f + 1, l + 1]