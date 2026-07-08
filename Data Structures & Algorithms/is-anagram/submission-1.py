class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        f1, f2 = {}, {}

        for i in range(len(s)):
            if s[i] not in f1:
                f1[s[i]] = 1
            else:
                f1[s[i]] += 1

            if t[i] not in f2:
                f2[t[i]] = 1
            else:
                f2[t[i]] += 1
        
        for key in f1.keys():
            if key not in f2.keys(): return False
            if f1[key] != f2[key]: return False

        return True
        



        
        