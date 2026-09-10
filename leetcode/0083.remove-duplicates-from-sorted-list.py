# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("+inf"))
        tail = dummy
        current = head
        while current:
            if tail.val != current.val:
                node = ListNode(current.val)
                tail.next = node
                tail = tail.next
            current = current.next
        return dummy.next
        