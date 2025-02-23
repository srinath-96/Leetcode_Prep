class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=[str(x) for x in digits]
        b="".join(a)
        c=list(str(int(b)+1))
        d=[int(x) for x in c]
        return d