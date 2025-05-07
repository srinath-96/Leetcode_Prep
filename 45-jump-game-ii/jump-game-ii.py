class Solution:
    def jump(self, nums: List[int]) -> int:
        far,end=0,0
        minju=0
        for n in range(len(nums)-1):
            far=max(far,n+nums[n])
            if n==end:
                end=far
                minju+=1
        return minju

