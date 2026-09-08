# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        slow, fast = current, current
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        prev = None
        current = slow.next
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # compare and check
        p1, p2 = head, prev
        is_palindrome = True
        while p1 and p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1 = p1.next
            p2 = p2.next
        return is_palindrome
