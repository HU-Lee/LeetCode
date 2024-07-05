# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        s = 0
        ans = ListNode(0)
        cur2 = ans
        while cur.next:
            cur2.val += cur.next.val
            if cur.next.val == 0:
                if cur.next.next:
                    cur2.next = ListNode(0)
                cur2 = cur2.next
            cur = cur.next
        return ans