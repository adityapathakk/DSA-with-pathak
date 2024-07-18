# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        maxDistance = 10

        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [0] * (maxDistance + 1)
            if not node.left and not node.right:
                res = [0] * (maxDistance + 1)
                res[1] = 1
                return res
            left = dfs(node.left)
            right = dfs(node.right)

            for i in range(1, distance + 1):
                for j in range(1, distance - i + 1):
                    self.count += left[i] * right[j]
            res = [0] * (maxDistance + 1)
            for i in range(1, maxDistance):
                res[i + 1] = left[i] + right[i]
            
            return res

        dfs(root)
        return self.count

'''

revise this question.
leetcode solution i referred to - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solutions/5493798/ultimate-1-ms-solution-beats-100-java-c-py-js-go-beginner-friendly-explanation/?envType=daily-question&envId=2024-07-18

'''
