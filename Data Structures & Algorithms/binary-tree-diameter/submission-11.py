# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def deep(node):
            if not node:
                return 0
            L = deep(node.left)
            R = deep(node.right)
            self.max_diameter = max(self.max_diameter,L + R)
            return max(L,R)+1
        deep(root)
        return self.max_diameter
        