class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"]": "[", "}": "{", ")": "("}
        for i in range(len(s)):
            if s[i] in pairs.values(): stack.append(s[i])
            elif s[i] in pairs.keys():
                if len(stack) == 0 or stack.pop() != pairs[s[i]]:
                    return False
        
        if not stack:
            return True
        return False