# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not r:
            return False
        if self.S(r,t):
            return True
        return self.isSubtree(r.left,t) or self.isSubtree(r.right,t) 
    def S(self, r: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not r and not t:
            return True
        if r and t and r.val==t.val:
            return self.S(r.left,t.left) and self.S(r.right,t.right)
        return False
        