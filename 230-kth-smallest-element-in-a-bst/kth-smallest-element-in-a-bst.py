class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=[]
        def dfs(root):
            if not root:
                return []
            dfs(root.left)
            a.append(root.val)
            dfs(root.right)
            return a
        x=dfs(root)
        x.sort()
        return x[k-1]