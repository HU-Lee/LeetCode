# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a,b,c = head, head.next, head.next.next
        idx = []
        mi = 1000000
        i = 1
        while c:
            if b.val < min(a.val, c.val) or b.val > max(a.val, c.val):
                if idx:
                    mi = min(mi, i - idx[-1])
                idx.append(i)
            i += 1
            a = a.next
            b = b.next
            c = c.next
        mx = idx[-1] - idx[0] if len(idx) > 1 else -1
        mi = -1 if mi == 1000000 else mi
        return [mi, mx]