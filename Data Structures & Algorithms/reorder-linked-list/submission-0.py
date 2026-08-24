# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        first = current.next
        while current.next:
            end = self.find_end(current)

            if end == first:
                current.next = end
                break
            current.next = end
            if not end:
                return
            current.next.next = first
            current = first
            first = current.next

        return
    
    
    def find_end(self, node):
        if not node.next:
            return node
        if node.next and not node.next.next:
            out = node.next
            node.next = None
            return out
        return self.find_end(node.next)