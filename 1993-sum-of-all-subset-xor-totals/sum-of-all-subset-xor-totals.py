class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def get_all_combinations(lst, r=None):
            """
            Get all possible combinations of elements in a list.
            If r is None, return combinations of all possible lengths.
            If r is specified, return combinations of that length only.
            """
            if not lst:
                return []
            
            if r is None:
                # Get combinations of all possible lengths
                result = []
                for i in range(1, len(lst) + 1):
                    result.extend(list(combinations(lst, i)))
                return result
            else:
                # Get combinations of specified length
                return list(combinations(lst, r))
        def xor_list(lst):
            if not lst:
                raise ValueError("List cannot be empty")
            
            # Initialize with first element
            result = lst[0]
            
            # XOR remaining elements
            for item in lst[1:]:
                result ^= item
            
            return result
        a=get_all_combinations(nums)
        sum=0
        for i in a:
            sum+=xor_list(i)
        return sum
            