# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        binaryTree = {} # values -> TreeNode pointers
        children = set() # all children stored in this set

        for p, c, l in descriptions: # parent value, child value, is list
            if p not in binaryTree:
                binaryTree[p] = TreeNode(p) # adding parent node if not already created
            if c not in binaryTree:
                binaryTree[c] = TreeNode(c) # adding child node if not already created
        
            if bool(l):
                binaryTree[p].left = binaryTree[c] # attaching child node to left branch
            else:
                binaryTree[p].right = binaryTree[c] # attaching child node to right branch
        
            children.add(c) # add child node value to children set
        
        for node in binaryTree.values():
            if node.val not in children: # if node not in children set, then it's the root node
                return node

''' Approach

Similar to Leetcode editorial - approach 3. when revising, check out other methods too.
link - https://leetcode.com/problems/create-binary-tree-from-descriptions/editorial
my Leetcode solution post link: https://leetcode.com/problems/create-binary-tree-from-descriptions/solutions/5480174/super-easy-code-with-comments-beats-67-runtime-85-9-memory/

'''
