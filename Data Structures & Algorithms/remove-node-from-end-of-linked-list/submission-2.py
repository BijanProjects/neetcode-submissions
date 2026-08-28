# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        put = self.counter(None, head, n)
        if put == n:
            return head.next
        
        return head

    def counter(self, prev, current, n):
        if not current.next:
            return 1

        out = self.counter(current, current.next, n)
        if out == n:
            current.next = current.next.next
            

        return 1 + out
