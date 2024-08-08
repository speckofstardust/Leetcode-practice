class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        res = 0

        while l<=r:
            if maxl < maxr:
                res += max(0, maxl-height[l])
                maxl = max(maxl, height[l])
                print(res, "maxl", maxl)
                l+=1
                
            else:
                res += max(0, maxr-height[r])
                maxr = max(maxr, height[r])
                print(res, "maxr", maxr)
                r-=1
        
        return res
        
