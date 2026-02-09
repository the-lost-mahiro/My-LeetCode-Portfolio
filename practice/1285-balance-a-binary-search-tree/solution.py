# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def createBackbone(root):
            temp = root
            size = 0

            while temp.right:
                if temp.right.left:
                    child = temp.right
                    temp.right = child.left
                    child.left = temp.right.right
                    temp.right.right = child
                
                else: 
                    temp = temp.right
                    size += 1
            
            return size
        
        def createBTree(root, size):
            m = (1 << int(math.log2(size + 1))) - 1
            compress(root, size - m)

            while m > 1:
                m = m // 2
                compress(root, m)
        
        def compress(root, count):
            scanner = root
            for _ in range(count):
                child = scanner.right

                if child:
                    scanner.right = child.right
                    scanner = scanner.right
                    child.right = scanner.left
                    scanner.left = child

                else:
                    break
        
        dummy = TreeNode(0)
        dummy.right = root

        size = createBackbone(dummy)
        createBTree(dummy, size)

        return dummy.right
