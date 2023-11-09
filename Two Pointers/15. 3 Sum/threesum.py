class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort -> fix one element -> find the other two with two pointer methos  
        ans=[]
        nums.sort()
        #print(nums)
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum=n+nums[j]+nums[k]
                if sum==0:
                    ans.append([n,nums[j],nums[k]])
                    j+=1
                    #need to check if the pointer points to a repeated element again, if one of them is checked, you don't need to check the other one cause n+(different number)+nums[k] will not be equal to 0
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
                    k-=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        return list(ans)
