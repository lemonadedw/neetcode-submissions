class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    result[index] = i - index
                else:
                    break
            
            stack.append(i)

        return result