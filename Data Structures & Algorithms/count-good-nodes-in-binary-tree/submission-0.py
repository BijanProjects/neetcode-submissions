# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(tree, val):
            if not tree:
                return 0
            if tree.val >= val:
                val = tree.val
                return 1 + helper(tree.left, val) + helper(tree.right, val)
            return helper(tree.left, val) + helper(tree.right, val)

        return helper(root, -150)