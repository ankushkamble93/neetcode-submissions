# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        total_diameter = 0
        def get_height(node: Optional[TreeNode]):
            nonlocal total_diameter
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            total_diameter = max(total_diameter, left_height+right_height)
            return 1 + max(left_height, right_height)
        get_height(root)
        return total_diameter
