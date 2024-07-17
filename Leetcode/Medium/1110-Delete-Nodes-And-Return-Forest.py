# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        setToDelete = set(to_delete) # converting list to set for constant time lookups
        forest = [] # list to store the roots of the resulting forest

        def dfs(node, is_root):
            if not node:
                return None
            rootDeleted = node.val in setToDelete
            if is_root and not rootDeleted:
                forest.append(node)
            node.left = dfs(node.left, rootDeleted) # recursively processing the left children
            node.right = dfs(node.right, rootDeleted) # recursively processing the right children
            return None if rootDeleted else node

        dfs(root, True) # starting DFS traversal from root
        return forest

''' Approach

revise this question.
The problem requires us to remove certain nodes from a binary tree and return the roots of the resulting forest.
By traversing the tree and handling deletions recursively, we can effectively manage the separations of the tree into multiple trees.
Each time we delete a node, its children (if any) become potential new roots of the trees in the forest.

'''
