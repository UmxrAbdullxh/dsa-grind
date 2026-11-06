# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Maintain two pointers slow and fast.
        Slow will point to kth node from beginning and fast will point to kth node from end
        Swap the values
        """
        dummy = ListNode(0, head)
        slow = dummy
        count = 0
        while slow and count < k:
            slow = slow.next
            count += 1
        fast = head
        slow2 = slow
        while slow2 and slow2.next:
            slow2 = slow2.next
            fast = fast.next
        # Swap values ?
        slow.val, fast.val = fast.val, slow.val
        return dummy.next
        