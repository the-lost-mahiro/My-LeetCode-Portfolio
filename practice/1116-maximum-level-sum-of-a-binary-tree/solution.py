# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        max_sum = float('-inf')

        queue = deque([root])
        cur_level = 0
        while queue:
            cur_level += 1
            cur_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            if cur_sum > max_sum:
                level = cur_level
                max_sum = cur_sum
        
        return level
