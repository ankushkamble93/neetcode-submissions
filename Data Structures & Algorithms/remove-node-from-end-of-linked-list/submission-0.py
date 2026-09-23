# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(curr: Optional[ListNode]):
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        reversed_head = reverse(head)
        dummy = ListNode(0, reversed_head)
        curr = dummy
        for _ in range(n-1):
            curr = curr.next
        curr.next = curr.next.next
        return reverse(dummy.next)
