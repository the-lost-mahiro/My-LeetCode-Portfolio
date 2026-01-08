# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(node, array):
            if not node.left and not node.right:
                array.append(node.val)
                return
            if node.left:
                getLeaf(node.left, array)
            if node.right:
                getLeaf(node.right, array)
        
        lvs1 = []
        lvs2 = []
        getLeaf(root1, lvs1)
        getLeaf(root2, lvs2)

        return lvs1 == lvs2
