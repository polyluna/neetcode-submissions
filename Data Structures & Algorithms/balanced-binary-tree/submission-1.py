# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            L = height(node.left)
            R = height(node.right)
            if L == -1 or R == -1 or abs(L - R) > 1:
                return -1
            return max(L,R) + 1
        return height(root) != -1