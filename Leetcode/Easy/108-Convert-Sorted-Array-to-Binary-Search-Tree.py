# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: # special case
            return None
        
        mid = len(nums) // 2 # middle element should be...
        root = TreeNode(nums[mid]) # ...the root
        root.left, root.right = self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]) # recursive method
        return root