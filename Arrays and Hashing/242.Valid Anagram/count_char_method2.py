class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        for c in s:
            if s.count(c)!=t.count(c):
                return False
        return True
        

