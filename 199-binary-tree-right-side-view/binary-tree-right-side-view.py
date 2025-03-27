# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def dfs(root,depth=0):
            if not root:
                return []
            if depth==len(a):
                a.append(root.val)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
            return a
        return dfs(root)