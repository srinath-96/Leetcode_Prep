class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        s1 = set(nums1) # forming a set of nums1 to omit out duplicates
        s2 = set(nums2) # forming a set of nums2 to omit out duplicates
        return (list(s1 -s2), list(s2 - s1)) # converting it into a list by
        