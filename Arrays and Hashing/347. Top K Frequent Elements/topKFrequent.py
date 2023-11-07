class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums={}
        for n in nums:
                count_nums[n]=1+count_nums.get(n,0)
        count_nums=dict(sorted(count_nums.items(), key=lambda x: x[1], reverse=True))
        lst=[i for i in count_nums.keys()]
        return lst[:k]
         
