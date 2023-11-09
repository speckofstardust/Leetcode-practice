class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[0]*len(height)
        for i in range(1,len(height)):
            if(height[i-1]>maxLeft[i-1]):
                maxLeft[i]=height[i-1]
            else:
                maxLeft[i]=maxLeft[i-1]
        #print(maxLeft)
        maxRight=[0]*len(height)
        minLR=[0]*len(height)
        for i in range(len(height)-2,-1,-1):
            if(height[i+1]>maxRight[i+1]):
                maxRight[i]=height[i+1]
            else:
                maxRight[i]=maxRight[i+1]
            minLR[i]=min(maxRight[i],maxLeft[i])
        #print(maxRight)
        #print(minLR)
        trappedWater=[max(0,(minLR[i]-height[i])) for i in range(len(height))]
        #print(trappedWater)
        return sum(trappedWater)
