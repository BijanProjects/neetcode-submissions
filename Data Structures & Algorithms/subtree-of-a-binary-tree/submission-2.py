# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.counter(root, subRoot)

    def counter(self, tree, sub):
        if self.isSame(tree, sub) == True:
            return True
        elif not tree and not sub:
            return True
        
        elif not tree or not sub:
            return False

        else:
            return self.counter(tree.left, sub) or self.counter(tree.right, sub)


    def isSame(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif not tree1 or not tree2:
            return False
        elif tree1.val != tree2.val:
            return False
        else:
            return self.isSame(tree1.left, tree2.left) and self.isSame(tree1.right, tree2.right)