# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.level = 0
        def search(root,curlevel):
            if root is None:
                return
            if self.level<curlevel:
                self.level = curlevel
            
            if root.left is not None:
                search(root.left,curlevel+1)
            if root.right is not None:
                search(root.right,curlevel+1)
        search(root,1)
        return self.level
        