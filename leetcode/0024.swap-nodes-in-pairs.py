# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (head and not head.next):
            return head
        dummy = ListNode(0, head)
        prev = dummy
        while prev and prev.next and prev.next.next:
            first = prev.next
            second = first.next
            # swap nodes
            temp = second.next
            second.next = first
            first.next = temp
            prev.next = second

            prev = first
        return dummy.next
