class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        di={")" : "(", "]" : "[", "}" : "{"  }
        for c in s:
            if c in di:
                if stack and stack[-1]==di[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False