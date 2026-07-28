# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        else:
            return self.check(p.left, q.left) and self.check(p.right, q.right) and p.val == q.val

    def check(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False

        if left.val != right.val:
            return False
        else:
            return self.check(left.left, right.left) and self.check(left.right, right.right)