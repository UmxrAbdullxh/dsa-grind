# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        counter = 1
        current = head
            
        prev1 = dummy
        while counter < left:
            prev1 = current
            counter += 1
            current = current.next
        tail = current
        # reverse
        prev = None
        while current and counter <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            counter += 1

        prev1.next = prev
        tail.next = current
        return dummy.next
        