# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = ListNode(0)
        lesser = ListNode(0)

        p1,p2 = greater, lesser

        while head:
            if(head.val < x):
                p2.next = head
                p2 = p2.next
            else:
                p1.next = head
                p1 = p1.next
            head = head.next

        p1.next = None
        p2.next = greater.next

        return lesser.next
      