# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        root1, root2 = [], []
        def helper(root:Optional[TreeNode], arr:list):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)
            helper(root.left, arr)
            helper(root.right, arr)
        helper(p, root1)
        helper(q, root2)
        return root1 == root2
        
        