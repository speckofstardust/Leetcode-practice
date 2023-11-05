class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t) 

        if len(s)!=len(t):
            return False
        count_s,count_t={},{}
        for i in range(len(s)):
            # dict.get(key, init_val): if the key is not already present in the dictionary, it initializes it with the value in init_val
            count_s[s[i]]=1+count_s.get(s[i],0) 
            count_t[t[i]]=1+count_t.get(t[i],0)
        for key in count_s:
            if count_s[key]!=count_t.get(key,0):
                return False
        return True
        

