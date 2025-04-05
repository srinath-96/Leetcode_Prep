class Solution:
    def romanToInt(self, s: str) -> int:
        s1={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        a=list(s)
        sum=0
        for i in range(len(s)):
            if i +1< len(s) and (s1[s[i]]<s1[s[i+1]]):
                sum-=s1[s[i]]
            else:
                sum+=s1[s[i]]
        return sum