class Solution:
    def isValid(self, s: str) -> bool:
        p = {')' : '(', '}' : '{', ']': '['}
        stack = []

        for c in s:
            if c in p.values():
                stack.append(c)
            elif c in p:
                if not stack or stack.pop() != p[c]:
                    return False
        
        return False if stack else True