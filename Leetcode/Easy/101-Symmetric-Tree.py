# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: # special case
            return True
        return self.isSame(root.left, root.right) # recursive method

    def isSame(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None: # if both root nodes are null nodes, we return true
            return True
        if leftRoot is None or rightRoot is None: # if only one of them is null, we return false
            return False
        if leftRoot.val != rightRoot.val: # if nodes don't have same value, return false
            return False
        return self.isSame(leftRoot.left, rightRoot.right) and self.isSame(leftRoot.right, rightRoot.left)