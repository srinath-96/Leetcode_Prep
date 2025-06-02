class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Create a hash map to store numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Return indices
            num_map[num] = i  # Store the number and its index in the hash map