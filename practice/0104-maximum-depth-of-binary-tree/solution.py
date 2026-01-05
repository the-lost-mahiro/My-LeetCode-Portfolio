# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            height = 0
            child = deque([root])
            while child:
                height += 1
                for _ in range(len(child)):
                    cur = child.popleft()
                    if cur.left != None:
                        child.append(cur.left)
                    if cur.right != None:
                        child.append(cur.right)
            return height
        return 0
