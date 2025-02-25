class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            res=max(res,r-l+1)
        return res