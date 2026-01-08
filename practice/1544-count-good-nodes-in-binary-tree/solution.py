# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def countGood(node, good):
            nonlocal count
            if node.val >= good:
                good = node.val
                count += 1
            if node.left:
                countGood(node.left, good)
            if node.right:
                countGood(node.right, good)
        
        countGood(root, float('-inf'))

        return count
