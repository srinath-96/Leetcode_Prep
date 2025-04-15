class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen:
            seen.add(n)
            if sum(int(digit)**2 for digit in str(n))==1:
                return True
            else:
                n=sum(int(digit)**2 for digit in str(n))
        return False
