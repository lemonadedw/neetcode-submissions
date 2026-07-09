class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(0, len(height) - 1):
            maxLeft[i + 1] = max(height[i], maxLeft[i])
        for i in range(len(height) - 1, 0, -1):
            maxRight[i - 1] = max(height[i], maxRight[i])

        minLR = [min(maxLeft[i], maxRight[i]) for i in range(len(height))]

        print(maxLeft)
        print(maxRight)
        print(minLR)

        for i, h in enumerate(height):
            total += minLR[i] - h if minLR[i] - h > 0 else 0

        return total