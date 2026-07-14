class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0
        pairs = []
        stack = []

        for p, s in zip(position, speed):
            pairs.append((p, s))
        
        pairs.sort()

        for p, s in pairs:
            time = (target - p) / s

            while stack and time >= stack[-1]:
                stack.pop()
            
            stack.append(time)
            
            # result += 1
            
        result += len(stack)

        return result