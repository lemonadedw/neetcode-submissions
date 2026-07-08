class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        char = set()
        max_length = 0

        for end in range(len(s)):
            while s[end] in char:
                char.remove(s[start])
                start += 1
            char.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length
            
        