# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev, self.ans = None, float('inf')
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.prev:
                self.ans = min(self.ans, root.val - self.prev.val)
            self.prev = root
            inorder(root.right)
            return
        
        inorder(root)
        return self.ans
    
# this question is the same as LC 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/