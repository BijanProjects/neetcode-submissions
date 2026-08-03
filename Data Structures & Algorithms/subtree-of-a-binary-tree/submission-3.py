# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(root, subRoot)


    def traverse(self, parent, sub):
        if self.isSame(parent, sub):
            return True
        elif not parent or not sub:
            return False
        else:
            return self.traverse(parent.left, sub) or self.traverse(parent.right, sub)

    def isSame(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif not tree1 or not tree2:
            return False
        elif tree1.val != tree2.val:
            return False
        else:
            return self.isSame(tree1.left, tree2.left) and self.isSame(tree1.right, tree2.right)

