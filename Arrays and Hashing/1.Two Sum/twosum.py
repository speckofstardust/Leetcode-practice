class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlst=[]
        for i in range(len(nums)):
            if target-nums[i] in numlst:
                return [i, nums.index(target-nums[i])]
            numlst.append(nums[i])
        
