# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # using fast and slow pointers to calculate the two halves of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half of the list
        second = slow.next

        #reverse the second half of the list
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # merge the two lists
        first, second = head, prev
        # choosing second because it is the smaller list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

