class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        
        print('freq:', freq)
        
        for i in range(0, len(s2) - len(s1) + 1):
            freq_check = {}
            for j in range(i, i + len(s1)):
                if s2[j] not in freq:
                    break
                
                freq_check[s2[j]] = 1 + freq_check.get(s2[j], 0)

            if freq_check == freq:
                return True
        
        return False