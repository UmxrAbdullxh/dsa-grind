# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        length = head
        while length:
            n += 1
            length = length.next
        if k == 0 or n == 0:
            return head
        point = n - (k % n)   # <-- number of nodes to keep at the front
        if point == n:
            return head
        p1 = head
        p1_len = 0
        while p1 and p1_len < point-1:
            p1_len += 1
            p1 = p1.next
        tail = p1.next
        p1.next = None
        p2 = tail
        while p2 and p2.next:
            p2 = p2.next
        if p2 != None:
            p2.next = head
        return tail
        