# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        """
        Loop through the list and check if next node has value equal to val?
        Keep a prev pointer and advance it with current. If current.val is equal to val then
        prev.next = current.next
        current.next = None
        """
        if not head:
            return None
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        while current:
            temp = current.next
            if current.val == val:
                prev.next = temp
                current.next = None
            if current.val != val:
                prev = current
            current = temp
        return dummy.next
        