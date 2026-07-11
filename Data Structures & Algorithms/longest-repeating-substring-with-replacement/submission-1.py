class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occur = defaultdict(int)
        count = 0

        l = 0
        for r in range(len(s)):
            occur[s[r]] += 1

            while (r - l + 1) - max(occur.values()) > k:
                occur[s[l]] -= 1
                l += 1
            
            count = max(r - l + 1, count)
    
        return count
