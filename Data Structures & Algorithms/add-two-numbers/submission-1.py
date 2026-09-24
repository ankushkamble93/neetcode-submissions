# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "", ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        
        # Reverse strings to form correct integers
        n1int = int(n1[::-1])
        n2int = int(n2[::-1])
        
        # Add integers and reverse the total string to construct the response
        total_str = str(n1int + n2int)[::-1]

        dummy = ListNode()
        curr = dummy
        for element in total_str:
            curr.next = ListNode(int(element))
            curr = curr.next
            
        return dummy.next