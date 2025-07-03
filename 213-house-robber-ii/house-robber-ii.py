class Solution:
    def rob(self, nums: List[int]) -> int:
        def t(nums):
            rob1,rob2=0,0
            for n in nums:
                t=max(rob1+n,rob2)
                rob1=rob2
                rob2=t
            return rob2
        
        return max(nums[0],t(nums[:-1]),t(nums[1:]))