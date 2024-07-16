# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right

''' Approach

revise this question - check solutions.
traverse to the left and check if we get the node else we will return none
if we get both p and q in different subtrees we will return the root because the common ancestor is the root.
otherwise, we will return p or q if p is the parent of q or q is the parent of p.

'''
