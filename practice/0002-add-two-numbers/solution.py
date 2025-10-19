# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        current = l1
        while current:
            a.append(current.val)
            current = current.next
        current = l2

        b=[]
        while current:
            b.append(current.val)
            current = current.next

        l = max(len(a), len(b))
        while len(a) < l:
            a.append(0)
        while len(b) < l:
            b.append(0)
        
        out = 0
        ans = []
        for i in range(l):
            ans.append(ListNode((a[i] + b[i] + out)%10))
            out = (a[i] + b[i] + out)//10

        if out != 0:
            ans.append(ListNode(out))

        for i in range(len(ans)-1):
            ans[i].next = ans[i+1]
        
        return ans[0]
