# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        if not head.next:
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reversed_list = self.reverse(slow.next)
        slow.next = None
        self.merge(head, reversed_list)

    def reverse(self, node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


    def merge(self, p, q):
        
        while q:
            next_p = p.next
            next_q = q.next
            p.next = q
            q.next = next_p
            p = next_p
            q = next_q





