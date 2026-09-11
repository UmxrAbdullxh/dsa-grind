# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode(0)
        odd = ListNode(0)

        p1, p2 = odd, even
        count = 1

        while head:
            if (count % 2 == 0):
                p2.next = head
                p2 = p2.next
            else:
                p1.next = head
                p1 = p1.next
            head = head.next
            count += 1
        

        p2.next = None
        p1.next = even.next

        return odd.next
        