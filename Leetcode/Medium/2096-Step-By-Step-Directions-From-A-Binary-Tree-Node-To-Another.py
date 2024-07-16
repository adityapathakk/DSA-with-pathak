# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findPath(self, node: TreeNode, target: int, path: List[str]) -> bool:
        if node is None:
            return False
        if node.val == target:
            return True
        
        path.append("L") # try left subtree
        if self.findPath(node.left, target, path):
            return True
        path.pop() # remove last character

        path.append("R") # try right subtree
        if self.findPath(node.right, target,path):
            return True
        path.pop() # remove last character
        
        return False
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath, destPath = [], []
        
        self.findPath(root, startValue, startPath) # find path from root to start node
        self.findPath(root, destValue, destPath) # find path from root to destination node

        directions = []
        commonPathLength = 0

        while commonPathLength < len(startPath) and commonPathLength < len(destPath)\
        and startPath[commonPathLength] == destPath[commonPathLength]: # find length of common path
            commonPathLength += 1
        
        # add "U" for each step to go up from start to common ancestor
        directions.extend("U" * (len(startPath) - commonPathLength))
        # add directions from common ancestor to destination
        directions.extend(destPath[commonPathLength:])
        
        return "".join(directions)

''' Approach

revise this question: see Leetcode editorial - approach 3.
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/editorial

'''
