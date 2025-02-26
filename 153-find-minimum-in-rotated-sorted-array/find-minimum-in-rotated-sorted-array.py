class Solution:
    def findMin(self, nums: List[int]) -> int:
        def rotate_right(arr, k):
            k = k % len(arr)  # Handle k > len(arr)
            return arr[-k:] + arr[:-k]
        minE=100
        l=0
        while l<len(nums):
            minE=min(minE,nums[0])
            nums=rotate_right(nums,1)
            l+=1
        return minE