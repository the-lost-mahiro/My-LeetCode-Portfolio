# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(node):
            if node.left:
                dfs(node.left)
                node.val += node.left.val
            if node.right:
                dfs(node.right)
                node.val += node.right.val
        
        dfs(root)
        
        prefixSum = root.val
        maxProduct = 0
        def cutEdge(node):
            nonlocal maxProduct
            if node.left:
                maxProduct = max(maxProduct, (prefixSum - node.left.val) * node.left.val)
                cutEdge(node.left)
            if node.right:
                maxProduct = max(maxProduct, (prefixSum - node.right.val) * node.right.val)
                cutEdge(node.right)
        
        cutEdge(root)

        return maxProduct % MOD
