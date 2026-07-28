# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return self.helper(left.left, right.left) and self.helper(left.right, right.right) and left.val == right.val