class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #map the charCount to a list if anagrams with dictionaries
        res=defaultdict(list)

        for s in strs:
            charCount=[0]*26
            for c in s:
                charCount[ord(c)-ord("a")]+=1
            res[tuple(charCount)].append(s)

        return res.values()
        
