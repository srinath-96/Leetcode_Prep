class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=nums[-1]
        nums2=[i for i in range(0,n+2)]
        a=list(set(nums) ^ set(nums2))
        return a[0]