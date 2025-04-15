class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1=collections.Counter(list(ransomNote))
        c2=collections.Counter(list(magazine))

        for keys in c1.keys():
            if keys not in c2.keys():
                return False
            else:
                if not c1[keys]<=c2[keys]:
                    return False
        return True
